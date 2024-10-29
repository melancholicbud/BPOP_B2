class TestClass:
    pow_val = 3 # variable of class
    def __init__(self, magic=10):
        self.magic = magic
    
    def square_magic(self):
        return self.magic ** TestClass.pow_val
    
if __name__ == "__main__":
    my_test1 = TestClass()
    print(my_test1.square_magic())
    my_test2 = TestClass(5)
    print(my_test2.square_magic())

print(TestClass)
print(my_test2.__class__)
print(my_test2.__class__.pow_val)
    