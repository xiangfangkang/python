import threading
import time

class ClassA(object):
    config = []
    @classmethod
    def setConfig(cls,config):
        cls.config = config
        print id(cls.config)
        print 'set'+str(cls.config)
    @classmethod
    def listeningHandler(cls):
        print id(cls.config)
        print 'lst'+str(cls.config)
    @classmethod
    def run(cls):
         t1=threading.Thread(target=cls.listeningHandler)
         t1.start()
         time.sleep(1)

if __name__ == '__main__':
    print 'ClassA Test'
    ClassA.run()
    
    
        
    
