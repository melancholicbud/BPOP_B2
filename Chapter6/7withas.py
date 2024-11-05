class MyError(Exception):
    pass

class TestWith:
    def print_value(self, value):
        print(f"Input value: {value}")
    
    def __enter__(self):
        print("Starting with block")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Success!")
        else:
            print("Exception: "+str(exc_type))
            return False

if __name__ == "__main__":
    with TestWith() as test_object:
        # starting with block
        test_object.print_value("Test 1")
        print("Ending with block")
    with TestWith() as test_object:
        test_object.print_value("Test 2")
        raise MyError("ERROR!")
        print("Ending with block")