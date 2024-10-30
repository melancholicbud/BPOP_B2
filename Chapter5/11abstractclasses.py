# assert
class AbstractBaseClass:
    def print_name(self):
        print("AbstractBaseClass")
    
    def action(self):
        assert False, "method, not define"

if __name__ == "__main__":
    my_class = AbstractBaseClass()
    my_class.print_name()
    # AssertionError
    # my_class.action()

# NotImplementedError
class AbstractClassEx:
    def print_name(self):
        print("AbstractBaseClass")
    
    def action(self):
        raise NotImplementedError("method not define")
    
if __name__ == "__main__":
    my_class = AbstractClassEx()
    my_class.print_name()
    # error
    # my_class.action()

class SubClass(AbstractClassEx):
    def action(self):
        print("method was defined")

if __name__ == "__main__":
    my_class = SubClass()
    my_class.print_name()
    my_class.action()