def custom_function1(a, b, c):
    print(a + b + c)
custom_function1(10, 4, 8)

def custom_function2(a, b, c=2):
    print(a + b + c)
custom_function2(b=1, c=4, a=4)

def custom_function3(a, b, c, *args):
    print(a + b + c + sum(*args))
custom_function3(1, 1, 1, [10, 20, 30])
# SyntaxError
# custom_function3(a=1, c=4, b=11,[10,20,30])

def custom_function4(a, b, c, *args, d):
    print(a + b + c + sum(*args) - d)
custom_function4(1, 1, 1, [10, 20, 30], d=4)
# TypeError
# custom_function4(1, 1, 1, [10, 20, 30], 4)

def custom_function5(*args, **kwargs):
    if args:
        print(args)
    if kwargs:
        print(kwargs)
custom_function5(10, 20, key='Hi', Oo = 100)

def custom_function6(*a, **b):
    if a:
        print(a)
    if b:
        print(b)
custom_function6(10, 20, key='Hi', Oo = 100)

def custom_function7(**kwargs):
    print(kwargs)
custom_function7(key='Hi!', Oo = 100)