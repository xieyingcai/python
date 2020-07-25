+ **知识储备**
[eventlet] (http://luckylau.tech/2017/03/06/Python%E7%9A%84eventlet%E4%BD%BF%E7%94%A8%E4%B8%8E%E7%90%86%E8%A7%A3/)

+  启动顺序  
'''python
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
            return deploy.loadapp("config:%s" % self.config_path, name=name)  #from paste import deploy
        except LookupError:
            LOG.exception("Couldn't lookup app: %s", name)
            raise PasteAppNotFound(name=name, path=self.config_path)

'''
-----------------------------------------------------------------------------------
最终的app是由pasteDeploy加载的  

通过配置文件处理后返回最终app  

[composite:neutron]
use = egg:Paste#urlmap
/: neutronversions_composite
/v2.0: neutronapi_v2_0

[composite:neutronapi_v2_0]
use = call:neutron.auth:pipeline_factory
noauth = cors http_proxy_to_wsgi request_id catch_errors osprofiler extensions neutronapiapp_v2_0
keystone = cors http_proxy_to_wsgi request_id catch_errors osprofiler authtoken keystonecontext extensions neutronapiapp_v2_0

[app:neutronapiapp_v2_0]
paste.app_factory = neutron.api.v2.router:APIRouter.factory
-----------------------------------------------------------------------------------
def pipeline_factory(loader, global_conf, **local_conf):
    """Create a paste pipeline based on the 'auth_strategy' config option."""
    pipeline = local_conf[cfg.CONF.auth_strategy]#默认是keystone认证方式
    pipeline = pipeline.split()
    filters = [loader.get_filter(n) for n in pipeline[:-1]]
    app = loader.get_app(pipeline[-1]) #即:neutronapiapp_v2_0
    filters.reverse()
    for filter in filters:
        app = filter(app)
    return app
-----------------------------------------------------------------------------------
def APIRouter(**local_config):
    return pecan_app.v2_factory(None, **local_config)
def _factory(global_config, **local_config):
    return pecan_app.v2_factory(global_config, **local_config)
setattr(APIRouter, 'factory', _factory)#给APIRouter设置属性并赋值为：_factory

-----------------------------------------------------------------------------------
def v2_factory(global_config, **local_config):
    # Processing Order:
    #   As request enters lower priority called before higher.
    #   Response from controller is passed from higher priority to lower.
    app_hooks = [
        hooks.UserFilterHook(),  # priority 90
        hooks.ContextHook(),  # priority 95
        hooks.ExceptionTranslationHook(),  # priority 100
        hooks.BodyValidationHook(),  # priority 120
        hooks.OwnershipValidationHook(),  # priority 125
        hooks.QuotaEnforcementHook(),  # priority 130
        hooks.NotifierHook(),  # priority 135
        hooks.QueryParametersHook(),  # priority 139
        hooks.PolicyHook(),  # priority 140
    ]
    app = pecan.make_app(root.V2Controller(),
                         debug=False,
                         force_canonical=False,
                         hooks=app_hooks,
                         guess_content_type_from_ext=True)
    startup.initialize_all()###########################初始化 Neutron Server
    return app
-----------------------------------------------------------------------------------
class V2Controller(object):

    # Same data structure as neutron.api.versions.Versions for API backward
    # compatibility
    version_info = {
        'id': 'v2.0',
        'status': 'CURRENT'
    }
    _load_version_info(version_info)

    # NOTE(blogan): Paste deploy handled the routing to the legacy extension
    # controller.  If the extensions filter is removed from the api-paste.ini
    # then this controller will be routed to  This means operators had
    # the ability to turn off the extensions controller via tha api-paste but
    # will not be able to turn it off with the pecan switch.
    extensions = ext_ctrl.ExtensionsController()

    @utils.expose(generic=True)
    def index(self):
        if not pecan.request.path_url.endswith('/'):
            pecan.abort(404)

        layout = []
        for name, collection in _CORE_RESOURCES.items():
            href = urllib.parse.urljoin(pecan.request.path_url, collection)
            resource = {'name': name,
                        'collection': collection,
                        'links': [{'rel': 'self',
                                   'href': href}]}
            layout.append(resource)
        return {'resources': layout}

    @utils.when(index, method='HEAD')
    @utils.when(index, method='POST')
    @utils.when(index, method='PATCH')
    @utils.when(index, method='PUT')
    @utils.when(index, method='DELETE')
    def not_supported(self):
        pecan.abort(405)

    @utils.expose()
    def _lookup(self, collection, *remainder):
        # if collection exists in the extension to service plugins map then
        # we are assuming that collection is the service plugin and
        # needs to be remapped.
        # Example: https://neutron.endpoint/v2.0/fwaas/firewall_groups
        if (remainder and
                manager.NeutronManager.get_resources_for_path_prefix(
                    collection)):
            collection = remainder[0]
            remainder = remainder[1:]
        controller = manager.NeutronManager.get_controller_for_resource(
            collection)
        if not controller:
            LOG.warning("No controller found for: %s - returning response "
                        "code 404", collection)
            pecan.abort(404)
        # Store resource and collection names in pecan request context so that
        # hooks can leverage them if necessary. The following code uses
        # attributes from the controller instance to ensure names have been
        # properly sanitized (eg: replacing dashes with underscores)
        request.context['resource'] = controller.resource
        request.context['collection'] = controller.collection
        # NOTE(blogan): initialize a dict to store the ids of the items walked
        # in the path for example: /networks/1234 would cause uri_identifiers
        # to contain: {'network_id': '1234'}
        # This is for backwards compatibility with legacy extensions that
        # defined their own controllers and expected kwargs to be passed in
        # with the uri_identifiers
        request.context['uri_identifiers'] = {}
        return controller, remainder