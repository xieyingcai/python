+ **知识储备**
[eventlet] (http://luckylau.tech/2017/03/06/Python%E7%9A%84eventlet%E4%BD%BF%E7%94%A8%E4%B8%8E%E7%90%86%E8%A7%A3/)

+  启动顺序  
    neutron-server = neutron.cmd.eventlet.server:main  
def main():  
    server.boot_server(wsgi_eventlet.eventlet_wsgi_server)  #boot_server执行eventlet_wsgi_server函数  
	
def eventlet_wsgi_server():
    neutron_api = service.serve_wsgi(service.NeutronApiService) #serve_wsgi主要是执行类service.NeutronApiService中的start方法，neutron_api就是service.NeutronApiService类实例
    start_api_and_rpc_workers(neutron_api)

def start_api_and_rpc_workers(neutron_api):
    try:
        worker_launcher = service.start_all_workers()

        pool = eventlet.GreenPool()
        api_thread = pool.spawn(neutron_api.wait)
        plugin_workers_thread = pool.spawn(worker_launcher.wait)

        # api and other workers should die together. When one dies,
        # kill the other.
        api_thread.link(lambda gt: plugin_workers_thread.kill())
        plugin_workers_thread.link(lambda gt: api_thread.kill())

        pool.waitall()
    except NotImplementedError:
        LOG.info("RPC was already started in parent process by "
                 "plugin.")

        neutron_api.wait()
	
def serve_wsgi(cls): #

    try:
        service = cls.create() #返回类实例
        service.start()
    except Exception:
        with excutils.save_and_reraise_exception():
            LOG.exception('Unrecoverable error: please check log '
                          'for details.')

    registry.publish(resources.PROCESS, events.BEFORE_SPAWN, service)
    return service  

class NeutronApiService(WsgiService):
    """Class for neutron-api service."""
    def __init__(self, app_name):
        profiler.setup('neutron-server', cfg.CONF.host)
        super(NeutronApiService, self).__init__(app_name)

    @classmethod
    def create(cls, app_name='neutron'):#通过类方法返回类实例
        # Setup logging early
        config.setup_logging()
        service = cls(app_name)
        return service

class WsgiService(object):
    def __init__(self, app_name):
        self.app_name = app_name
        self.wsgi_app = None

    def start(self):
        self.wsgi_app = _run_wsgi(self.app_name)

    def wait(self):
        self.wsgi_app.wait()

def _run_wsgi(app_name):
    app = config.load_paste_app(app_name)
    if not app:
        LOG.error('No known API applications configured.')
        return
    return run_wsgi_app(app)
	
def load_paste_app(app_name):
    """Builds and returns a WSGI app from a paste config file.

    :param app_name: Name of the application to load
    """
    loader = wsgi.Loader(cfg.CONF)

    # Log the values of registered opts
    if cfg.CONF.debug:
        cfg.CONF.log_opt_values(LOG, logging.DEBUG)
    app = loader.load_app(app_name)
    return app
	
class Loader(object):
    """Used to load WSGI applications from paste configurations."""

    def __init__(self, conf):
        """Initialize the loader, and attempt to find the config.

        :param conf: Application config
        :returns: None

        """
        conf.register_opts(_options.wsgi_opts)
        self.config_path = None

        config_path = conf.api_paste_config
        if not os.path.isabs(config_path):
            self.config_path = conf.find_file(config_path)
        elif os.path.exists(config_path):
            self.config_path = config_path

        if not self.config_path:
            raise ConfigNotFound(path=config_path)
			
	def load_app(self, name): #最终
        """Return the paste URLMap wrapped WSGI application.

        :param name: Name of the application to load.
        :returns: Paste URLMap object wrapping the requested application.
        :raises: PasteAppNotFound

        """
        try:
            LOG.debug("Loading app %(name)s from %(path)s",
                      {'name': name, 'path': self.config_path})
            return deploy.loadapp("config:%s" % self.config_path, name=name)
        except LookupError:
            LOG.exception("Couldn't lookup app: %s", name)
            raise PasteAppNotFound(name=name, path=self.config_path)