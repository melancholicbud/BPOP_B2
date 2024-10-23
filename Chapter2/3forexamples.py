for it in ['first', 'second', 4, 5.9, 'finish']:
    print(it, end=' ')

my_str = 'in far-far space odyssey...'
for it in my_str:
    print(it, end='-')

my_str = ('in', 'far-', 'far', 'space', 'odyssey')
for it in my_str:
    print(it, end=' ')

my_tuple_list = [(3,6), (0,1), (4,5), ('0',3.9)]
for (a,b) in my_tuple_list:
    print(a, b)

# value extraction via iterated key
my_dict = {'a': 1, 'b': 10, 'c': 3.8}
for key in my_dict:
    print(key, '=>', my_dict[key])

# iteration by 'key:value' pair
for key, value in my_dict.items():
    print(key, '=>', value)

items = ("aaa", 111, (4, 5), 2.01)
tests = [(4, 5), 3.14]
for key in tests:
    for item in items:
        if item == key:
            print(key, 'found')
            break
else:
    print(key, 'does not found')