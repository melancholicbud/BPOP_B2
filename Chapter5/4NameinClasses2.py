class TestClass:
    pow_val = 3 # variable of class
    def __init__(self, magic=10):
        self.magic = magic
    
    def new_square_magic(self):
        return self.magic ** self.__class__.pow_val
    
if __name__ == "__main__":
    my_test1 = TestClass()
    print(my_test1.new_square_magic())
    my_test2 = TestClass(5)
    print(my_test2.new_square_magic())

print(TestClass)
print(my_test2.__class__)
print(my_test2.__class__.pow_val)

my_test3 = TestClass()
my_test4 = TestClass()
my_test3.pow_val = 10
print(my_test3.pow_val)
print(my_test4.pow_val)

my_test5 = TestClass()
TestClass.pow_val = 40
print(my_test5.pow_val)