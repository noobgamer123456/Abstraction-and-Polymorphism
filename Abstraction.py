from abc import ABC, abstractmethod

class absclass(ABC):
    
    def print(self,x):
        print("Passed value:", x)
        
    @abstractmethod
    def task(self):
        print("We are inside absclass task")
        
class testClass(absclass):
    def task(self):
        print("We are inside test_class task")
        
        
testObj = testClass()
testObj.task()

testObj.print(100)

print()
o1 = absclass()
o1.task()