class MyClass:
    def get_String(self):
        self.s = input("Enter a string: ")
    def print_String(self):
        print(self.s.upper())

obj = MyClass()
obj.get_String()
obj.print_String()
