my_tuple = ('Alex', 'John')
my_tuple = tuple(['Alex', 'John'])
my_tuple = 'Alex', 'John'
my_tuple = ()

my_tuple = (2+3)*2
print(type(my_tuple))
my_tuple = (2, 3)
print(type(my_tuple))

my_tuple = 2, 3, 4, 5
print(my_tuple)
my_list = list(my_tuple)
print(my_list)
my_list = list(map(lambda x: x*2, my_list))
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

# typeerror
# my_tuple[0] = 3

from collections import namedtuple
ItemRec = namedtuple('ItemRec', ['name', 'age', 'jobs'])
my_tuple = ItemRec('Nazar', age=21, jobs=['student', 'developer'])
print(my_tuple)
print(my_tuple[0], my_tuple[2])
print(my_tuple.name, my_tuple.jobs)

my_dict = my_tuple._asdict()
print(my_dict['name'], my_dict['jobs'])
print(my_dict)