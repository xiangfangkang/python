import try1try.p1.ClassA as A

class ClassB(object):
    @classmethod
    def run(cls):
        A.ClassA.setConfig([123,456])
        
if __name__ == '__main__':
    print 'ClassB Test'
    ClassB.run()
