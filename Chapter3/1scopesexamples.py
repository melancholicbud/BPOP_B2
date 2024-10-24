X = 4
def test_func1(y):
    print(X + y)
test_func1(4)

def test_func2(y):
    X = 3
    print(X + y)
test_func2(4)
print(X)

def test_func3(y):
    global X
    X = 3
    print(X + y)
test_func3(4)
print(X)