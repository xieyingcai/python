+ TaskSet、TaskSetMeta
  编写的测试例一般都会继承与TaskSet，并将该继承了TaskSet的类赋值给类Locust中的task_set属性
  Demo.py  
```python
  from locust import HttpLocust, TaskSet
  def login(l):
      l.client.post("/login", {"username":"ellen_key", "password":"education"})

  def logout(l):
      l.client.post("/logout", {"username":"ellen_key", "password":"education"})

  def index(l):
      l.client.get("/")

  def profile(l):
      l.client.get("/profile")
      
  class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)
        
  class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
```
  TaskSetMeta是一个元类，通过TaskSetMeta来创建Taskset类。Taskset中有tasks属性，通过元类TaskSetMeta重新构造之后，Taskset中的tasks属性有了新的值。  
  该值主要是通过其权重进行多次复制。  
  比如上面的UserBehavior类的tasks属性的值实际上是：[index,index,profile]  
```
  class TaskSetMeta(type):
      def __new__(mcs, classname, bases, classDict):
        new_tasks = []
        for base in bases:
            if hasattr(base, "tasks") and base.tasks:
                new_tasks += base.tasks
        
        if "tasks" in classDict and classDict["tasks"] is not None:
            tasks = classDict["tasks"]
            if isinstance(tasks, dict):
                tasks = six.iteritems(tasks)
            
            for task in tasks:
                if isinstance(task, tuple):
                    task, count = task
                    for i in xrange(0, count):
                        new_tasks.append(task)
                else:
                    new_tasks.append(task)
        
        for item in six.itervalues(classDict):
            if hasattr(item, "locust_task_weight"):
                for i in xrange(0, item.locust_task_weight):
                    new_tasks.append(item)
        
        classDict["tasks"] = new_tasks
        
        return type.__new__(mcs, classname, bases, classDict)
```
+ load_locustfile  
   load_locustfile函数是返回指定路径下文件中继承了Locust(具有task_set属性且有已经赋值)的类，  
   比如指定的目录下面含有上面的Demo.py文件，将返回类：WebsiteUser  
 ```python
   def load_locustfile(path):
      ...
      locusts = dict(filter(is_locust, vars(imported).items()))#函数式编程，locusts是一个
      return imported.__doc__, locusts
   
   def is_locust(tup):
    name, item = tup
    return bool(
        inspect.isclass(item)
        and issubclass(item, Locust)
        and hasattr(item, "task_set")
        and getattr(item, "task_set")
        and not name.startswith('_')
    )
 ```
