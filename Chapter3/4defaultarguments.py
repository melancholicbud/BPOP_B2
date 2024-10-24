def test_default(a=10):
    print(a)
test_default('Hi!')
test_default()

def test_default2(a=10, b=12):
    print(a+b)

test_default2()
test_default2(4)
test_default2(4, 2)

def test_default3(a, b=12):
    print(a+b)
test_default3(4)
test_default3(4, 2)

# SyntaxError
"""
def test_default4(b=12, a):
    print(a+b)
test_default4(4, 2)
"""