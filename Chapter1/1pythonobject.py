i = 5
print(isinstance(i, object))
print(isinstance('Oo', object))
print(isinstance([2, 4, 't'], object))
print(isinstance({'a': 3, 'b': 5}, object))
print(isinstance((2, 4, 'w'), object))

def test_func():
    pass
print(isinstance(test_func, object))