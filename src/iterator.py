from abc import ABC, abstractmethod

class Iterator(ABC):

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def reset(self):
        pass

class MyIterator(Iterator):

    
    @staticmethod
    def static_method():
        print("hello world")
    
    def __init__(self, arr):
        self.x = arr
        self.i = 0

    def reset(self):
        self.i = 0

    def has_next(self):
        return self.i < len(self.x)
    
    def next(self):
        v = self.x[self.i]
        self.i+=1
        return v


xx = MyIterator([1,2,3])
print(xx.x)
while(xx.has_next()):
    print (xx.next())

