type1 = []
type2 = list()

type1 = ['one', 'two']
type2 = list(['one', 'two'])

my_list = list(['one', 'two'])
print(my_list)
my_list.append('three')
print(my_list)

my_list.append(4)
my_list.append(5)
print(my_list)

from typing import List, Dict

def foo(a: str, b: int):
    return len(a) - b
my_new_list: List[int] = [4,5]
my_new_list.append('add')
print(my_new_list)

# special error: TypeError
"""for it in my_new_list:
    it = it - 1
"""

# print(foo(False, 'sdasd'))

names = ['Nazar', 'Maxim', 'Alex']
print(names)
names.insert(1, 'John')
print(names)

one = [1, 2]
two = [3, 4]
one.extend(two)
print(one)

# the same as names.remove('Maxim') or names.pop(2)
del names[2]
print(names)

names.sort()
print(names)

# typeerror
new_array = [2, 'abc', 'ttt', '10', 3.6]
# new_array.sort()


new_array.sort(key=str)
print(new_array)

my_list=[1, 2, 2, 3, 2]
print(my_list.count(2))

my_array = [2, 3, 5, 7, 8, 10]
print(my_array)
my_new_array = my_array
my_new_array.append(12)
print(my_array)

my_array = [2, 3, 5, 7, 8, 10]
print(my_array)
my_new_array = my_array.copy()
my_new_array.append(12)
print(my_array)

my_array = [2, 3, 5, 7, 8, 10]
print(my_array)
my_new_array = my_array.copy()
my_new_array.append(12)
print(my_array)
print(my_new_array)

print(2 in my_array)
print(0 in my_array)