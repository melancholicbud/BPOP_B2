my_add = lambda x, y: x+y
print(my_add(1, 2))
# equivalent:
"""
def my_add(x, y):
    return x+y
print(my_add(1, 2))
"""

print((lambda x, y: x+y)(1,2))

list_tuples = [('d', 4), ('b', 2), 
               ('a', 1), ('c', 3), 
               ('a', 0)]
print(sorted(list_tuples))
print(sorted(list_tuples, key=lambda x: x[1]))
print(sorted(list_tuples, key=lambda x: x[0]))

# or
print(sorted(range(-5, -6), key=lambda x: x * x))
print(sorted(range(-5, -6), key=lambda x: x ** x))