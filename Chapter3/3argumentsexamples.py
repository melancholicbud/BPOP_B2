def test1(a, b, c):
    print('a = {}; b = {}; c = {}'.format(a, b, c))

x, y, z = (1, [2, 10], 'Hi!')
test1(x, y, z)
print('x = {}, y = {}; z = {}'.format(x, y, z))

def test2(a, b, c):
    print('a = {}; b = {}; c = {}'.format(id(a), id(b), id(c)))

x, y, z  = (1, [2, 10], 'Hi!')
test2(x, y, z)
print('x = {}; y = {}; z = {}'.format(id(x), id(y), id(z)))

def test3(a, b, c):
    a = 5
    b[0] = 'Oo'
    c = '(-_-)'
    print('a = {}; b = {}; c = {}'.format(a, b, c))
    print('a = {}; b = {}; c = {}'.format(id(a), id(b), id(c)))

x, y, z = (1, [2, 10], 'Hi!')
test3(x, y, z)
print('x = {}; y = {}; z = {}'.format(x, y, z))
print('x = {}; y = {}; z = {}'.format(id(x), id(y), id(z)))


x, y, z = 1, [2, 10], 'Hi!'
a, b, c = x, y, z
print('a = {}; b = {}; c = {}'.format(id(a), id(b), id(c)))
print('x = {}; y = {}; z = {}'.format(id(x), id(y), id(z)))
a = 5
b[0] = 'Oo'
c = '(-_-)'
print('a = {}; b = {}; c = {}'.format(a, b, c))
print('x = {}; y = {}; z = {}'.format(x, y, z))
print('a = {}; b = {}; c = {}'.format(id(a), id(b), id(c)))
print('x = {}; y = {}; z = {}'.format(id(x), id(y), id(z)))

one = 4
two = one
three = 4
print('one = {}; two = {}; three = {}'.format(id(one), id(two), id(three)))
print(id(one) == id(two) == id(three))