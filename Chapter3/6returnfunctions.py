def test_return1(a, b):
    c = a + b
print(test_return1(2, 4))

def test_return2(a, b):
    return a + b
print(test_return2(2, 4))

def test_return3(a, b):
    c = a + b
    m = a * b
    e = a ** b
    d = a / b
    s = a - b
    return c, m, e, d, s
print(test_return3(4, 2))
x, y, q, w, z = test_return3(4, 2)
print(x, y, q, w, z)
_, *my_list, _ = test_return3(4, 2)
print(my_list)
y, *my_list, q = test_return3(4, 2)
print(y, my_list, q)
w, _, _, *my_list = test_return3(4, 2)
print(w, my_list)
# ValueError
"""
w, _ = test_return3(4, 2)
print(w, my_list)
"""
# SyntaxError
# *first, *second = test_return3(4, 2)