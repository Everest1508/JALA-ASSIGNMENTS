class Overloading:
    def overloading_method1(self, param1, param2=None, param3=None):
        if param2 is None and param3 is None:
            print(f"Method with one parameter: {param1}")
        elif param3 is None:
            print(f"Method with two parameters: {param1}, {param2}")
        else:
            print(f"Method with three parameters: {param1}, {param2}, {param3}")

    def overloading_method2(self, param1, param2=None):
        if param2 is None:
            print(f"Method with one parameter of type int: {param1}")
        else:
            print(f"Method with two parameters of types str and int: {param1}, {param2}")

# Instantiate the class and call the methods
obj = Overloading()
obj.overloading_method1("Value1")
obj.overloading_method1("Value1", "Value2")
obj.overloading_method1("Value1", "Value2", "Value3")
obj.overloading_method2("Value1")
obj.overloading_method2("Value1", 42)
