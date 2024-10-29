class TestClass:
    """Class pew-pew"""
    all_created_classes = []
    def __init__(self, magic=10):
        """creating an instance of a class"""
        self.magic = magic
        # TestClass.all_created_classes(self)
        self.__class__.all_created_classes.append(self)
    
    def square_magic(self):
        """Squaring"""
        return self.magic ** 2
    
    @classmethod
    def sum_all_square_magic(cls):
        """Class method of count of squares all TestClasses"""
        result = 0
        for it in cls.all_created_classes:
            result += it.square_magic()
        return result
    
if __name__ == "__main__":
    my_test1 = TestClass()
    my_test2 = TestClass(5)
    my_test3 = TestClass(15)
    print(TestClass.sum_all_square_magic())
    my_test4 = TestClass(1)
    print(TestClass.sum_all_square_magic())