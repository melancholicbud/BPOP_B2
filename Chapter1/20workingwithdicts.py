my_dict = {}
# two-element dictionary
my_dict = {'name': 'Alex', 'course': 3}
# inserting
my_dict = {'info': {'name': 'Alex', 'course':3}}
# alternative variants creating: keywords,
# pair "key:variable", packed pairs "key:variable"
# list of keys
my_dict = dict(name='Alex', course=3)
my_dict = dict([('name', 'Alex'), ('course', '3')])
# for some reason - doens't work
# my_dict = dict(zip(keyslist, valueslist))
my_dict = dict.fromkeys(['name', 'course'])

my_dict = {}
my_dict['name'] = 'Alex'
my_dict['course'] = 3
print(my_dict)
print(my_dict['name'])
# keyerror
# print(my_dict['info'])
print('info' in my_dict)
print('name' in my_dict)

print(my_dict.get('name', 'Maxim'))
print(my_dict.get('info', 'no'))
my_dict.setdefault('info', 'default')
print(my_dict['info'])
my_dict.setdefault('name', 'default')
print(my_dict['name'])

my_dict = {'name': 'Nazar', 'course' : 3,  
           'info': {'age': 21, 'country': 'UA'}}
# output all keys
print(list(my_dict.keys()))
# output all variables
print(list(my_dict.values()))
# tuples of pair "key:variable"
print(list(my_dict.items()))

# copy dicts
my_dict = {'name': 'Nazar', 'course' : 3}
my_new_dict = my_dict.copy()
my_new_dict['info'] = 'None'
print(my_dict)
print(my_new_dict)

my_dict = {'name': 'Nazar', 'course' : 3,  
           'info': {'age': 21, 'country': 'UA'}}
print(my_dict)
my_new_dict = my_dict.copy()
my_new_dict['info']['age'] = 1
print(my_dict)

# deep copy
import copy
my_dict = {'name': 'Nazar', 'course' : 3,  
           'info': {'age': 21, 'country': 'UA'}}
my_new_dict = copy.deepcopy(my_dict)
my_new_dict['info']['age'] = 1
print(my_dict)
print(my_new_dict)

my_dict = {'name': 'Alex', 'course': 3, 'test1' : 10, 
           'test2': 'prob', 'test3': 3.56}
print(my_dict)
# if test3 is not in dict, dict keeps the same and output 10
print(my_dict.pop('test3', 10))
print(my_dict)
print(my_dict.pop('test3', 10))
# deleting/returning any pair (key:variable)
print(my_dict.popitem())
del my_dict['name']
print(my_dict)

# joining two dicts
my_dict = {'name': 'Alex', 'course' : 3}
my_new_dict = {'test1' : 10, 'test2' : 'prob', 'test3' : 3.56}
my_dict.update(my_new_dict)
print(my_dict)
