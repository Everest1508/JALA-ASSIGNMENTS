#1: Class with Constructors
class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default Constructor called.")
        elif arg1 is not None and arg2 is None:
            print(f"Name: {arg1}")
        elif arg1 is not None and arg2 is not None:
            print(f"Full Name: {arg1} {arg2}")

# Instantiate the class to call all constructors
obj1 = MyClass()
obj2 = MyClass("Ritesh")
obj3 = MyClass("Ritesh", "Mahale") 

#2: Superclass from Child Class
class ParentClass:
    def __init__(self):
        print("ParentClass Constructor called.")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        print("ChildClass Constructor called.")

child_obj = ChildClass()

#3: Apply Access Modifiers to Constructor
class AccessModifiersExample:
    def __init__(self):
        self.public_var = "Public Variable"
        self._protected_var = "Protected Variable"
        self.__private_var = "Private Variable"

obj = AccessModifiersExample()
print(obj.public_var)
print(obj._protected_var)
print(obj._AccessModifiersExample__private_var)

# 4: Illustrate the Concept of Attributes of a Constructor
class ConstructorAttributesExample:
    def __init__(self, attr1, attr2):
        self.attribute1 = attr1
        self.attribute2 = attr2

obj = ConstructorAttributesExample("Ritesh", "Mahale")

print(obj.attribute1)
print(obj.attribute2)
