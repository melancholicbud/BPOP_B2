def free_decorator(function):
    return function

def my_func1():
    return "It's work!!!"
my_func1 = free_decorator(my_func1)
my_func1()

@free_decorator
def my_func2():
    return "It's work!!!"
my_func2()

def up_register(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@up_register
def my_func3():
    return "It's work!!!"
my_func3()

def h1_html(function):
    def wrapper():
        return '<h1>' + function() + '</h1>'
    return wrapper

def body(function):
    def wrapper():
        return '<body>' + function() + '</body>'
    return wrapper

@body
@h1_html
def my_func4():
    return "It's work!!!"
print(my_func4())

my_decfunc = body(h1_html(my_func4))
print(my_decfunc)

# here is a TypeError
"""
def body2(function):
    def wrapper2():
        return '<body>' + function() + '</body>'
    return wrapper2

@body2
def my_func5(name):
    return name+", It's Work!!!"
my_func5('Alex')
"""
# for fixing
def body3(function):
    def wrapper3(name):
        return '<body>' + function(name) + '</body>'
    return wrapper3

@body3
def my_func6(name):
    return name+", It's work!!!"
my_func6('Alex')

def proxy1(function):
    def wrapper4(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper4

def my_func7(name = "Alex", line="It's work!!!"):
    return f'{name}, {line}'

def proxy2(func):
    def wrapper5(*args, **kwargs):
        print(f'TRACING: called'
              f' {func.__name__}() '
              f'c {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACING: {func.__name__}() returned {original_result!r}')
        return original_result
    return wrapper5

print(my_func7())
print(my_func7('Jon'))
print(my_func7(line="^_^", name='Jon'))
print(my_func7("Fine", "you win!!!"))