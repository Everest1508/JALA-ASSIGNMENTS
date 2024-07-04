from abc import ABC, abstractmethod

# Abstract class
class MyAbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
    
    def non_abstract_method(self):
        print("This is a non-abstract method.")

# Subclass for the abstract class
class MySubClass(MyAbstractClass):
    def abstract_method(self):
        print("This is the implementation of the abstract method in the subclass.")

# child class
child_object = MySubClass()

# non-abstract method
child_object.non_abstract_method()

# instance in the child class
child_object.abstract_method()

# instance for the child class in the child class
child_object_in_child = MySubClass()

# the child class
child_object_in_child.non_abstract_method()
