class ParentClass:
    def __init__(self):
        self.__private_field1 = "Private Field 1"
        self.__private_field2 = "Private Field 2"

    def __private_method(self):
        print("Private Method")

    def main_method(self):
        print("Accessing private fields from the main method:")
        print("Field 1:", self.__private_field1)
        print("Field 2:", self.__private_field2)
        print("\nCalling private method from the main method:")
        self.__private_method()


class SubClass(ParentClass):
    def access_private_members(self):
        # Attempt to access private fields and method from the subclass
        print("\nAttempting to access private members from the subclass:")
        # AttributeError
        # print("Field 1 from SubClass:", self.__private_field1)
        # print("Field 2 from SubClass:", self.__private_field2)
        # self.__private_method()  # AttributeError


# Create an object of the ParentClass and run the main method
parent_obj = ParentClass()
parent_obj.main_method()

# Create an object of the SubClass and attempt to access private members
subclass_obj = SubClass()
subclass_obj.access_private_members()
