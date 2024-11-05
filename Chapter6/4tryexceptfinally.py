def example_1(text):
    try:
        text[99]
    except IndexError:
        print('except')
    finally:
        print('finally')
    print('after try')

def example_2(text):
    try:
        text[3]
    except IndexError:
        print('except')
    else:
        print('else')
    finally:
        print('finally')
    print('after try')

def example_3(text):
    try:
        text[3]
    except IndexError:
        print('except')
    finally:
        print('finally')
    print('after try')

def example_4():
    try:
        my_error = 1/0
    except IndexError:
        print('except')
    finally:
        print('finally')
    print('after run')

def example_5():
    file = open('data', 'w')
    try:
        raise FileNotFoundError # generating an exception
    finally:
        print('finally')
    file.close() # always closing a file for reset buffer count
    print('after try')

if __name__ == "__main__":
    my_text = "Test"
    print("run example 1")
    example_1(my_text)
    print("run example 2")
    example_2(my_text)
    print("run example 3")
    example_3(my_text)
    print("run example 4")
    # ZeroDivisionError
    # example_4()
    print("run example 5")
    # FIleNotFoundError
    # example_5()
    print("Continuing...")