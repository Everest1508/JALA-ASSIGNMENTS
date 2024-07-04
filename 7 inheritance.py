class A:
    def __init__(self):
        self.var_a = "A"

    def method_a1(self):
        print("Method A1 in class A")

    def method_a2(self):
        print("Method A2 in class A")

    def overridden_method(self):
        print("Overridden method in class A")


class B(A):
    def __init__(self):
        super().__init__()
        self.var_b = "B"

    def method_b1(self):
        print("Method B1 in class B")

    def method_b2(self):
        print("Method B2 in class B")

    def overridden_method(self):
        print("Overridden method in class B")


class C(B):
    def __init__(self):
        super().__init__()
        self.var_c = "C"

    def method_c1(self):
        print("Method C1 in class C")

    def method_c2(self):
        print("Method C2 in class C")

    def overridden_method(self):
        print("Overridden method in class C")


class MainClass:
    def main(self):
        obj_a = A()
        obj_b = B()
        obj_c = C()

        # Call methods of class A
        obj_a.method_a1()
        obj_a.method_a2()
        obj_a.overridden_method()

        print("\n")

        # Call methods of class B
        obj_b.method_a1()
        obj_b.method_b1()
        obj_b.method_b2()
        obj_b.overridden_method()

        print("\n")

        # Call methods of class C
        obj_c.method_a1()  
        obj_c.method_b1()  
        obj_c.method_c1()
        obj_c.method_c2()
        obj_c.overridden_method()

        print("\n")

        # Runtime polymorphism
        print(f"Var A: {obj_a.var_a}")
        print(f"Var B: {obj_b.var_b}")
        print(f"Var C: {obj_c.var_c}")

        # Overridden method with super class reference
        print("\nCalling overridden method with super class reference:")
        super_ref_b = B()
        super_ref_c = C()
        super_ref_b.overridden_method()  
        super_ref_c.overridden_method()  


main_obj = MainClass()
main_obj.main()
