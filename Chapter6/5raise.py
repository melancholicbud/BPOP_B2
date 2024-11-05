class TestException(Exception):
    pass

class NewTestException(Exception):
    pass

if __name__ == "__main__":
    try:
        try:
            raise IndexError("my error")
        except IndexError as ex:
            print("Exception handling")
            raise TestException("Handle!") from ex
    except TestException as ex:
        raise NewTestException("One more Handle!") from ex
    print("Working on!")
    