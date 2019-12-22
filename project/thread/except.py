#! python3
#-*- coding:utf-8 --
'''
Created on 2019年7月7日

@author: Administrator
'''
import threading
from _ast import Raise
from time import sleep

class ExcThread(threading.Thread):
    def __init__(self,group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        if kwargs is None:
            kwargs = {}
        self.__target = target
        self.__args = args
        self.__kwargs = kwargs
        
    def run(self):
        self.exc = None
        try:
            # Possibly throws an exception
            if self.__target:
                self.__target(*self.__args, **self.__kwargs)
        except Exception as e:
            import sys
            self.exc = sys.exc_info()
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self.__target, self.__args, self.__kwargs
    # Save details of the exception thrown but don't rethrow,
    # just complete the function
    
    def join(self):
        threading.Thread.join(self)
        if self.exc:
            msg = "Thread '%s' threw an exception: %s" % (self.getName(), self.exc[1])
            new_exc = Exception(msg)
            raise new_exc.with_traceback(self.exc[2])

def test1():
    for i in range(2):
        print('{},{}'.format(threading.current_thread().getName(), i))
    raise RuntimeError('success')
def test2():
    for i in range(5):
        print('{},{}'.format(threading.current_thread().getName(), i))
        sleep(1)

if __name__ == '__main__':

    while True:
        th = ExcThread(target=test1)
        th2 = ExcThread(target=test2)
        try:
            th.start()
            th2.start()
            th.join()
            th2.join()
        except Exception as e:
            print(e)
            break
    print('Done')