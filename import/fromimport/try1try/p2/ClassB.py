from try1try.p1.ClassA import ClassA

class ClassB(object):
    @classmethod
    def run(cls):
        ClassA.setConfig([123,456])
        
if __name__ == '__main__':
    print 'ClassB Test'
    ClassB.run()
