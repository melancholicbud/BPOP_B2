""" this code can be written better:
my_list = [1, 2, 3, 4, 5]
for i in range (len(my_list)):
    my_list[i] += 10
print(my_list)
"""
my_list = [1, 2, 3, 4, 5]
my_list = [it+10 for it in my_list]
print(my_list)

""" wrote by for:
my_list = [1, 2, 3, 4, 5]
new_list = []
for it in my_list:
    new_list.append(it + 10)
print(new_list)
"""

new_list = [x for x in range(10) if x % 2 != 0]
print(new_list)

# more hard logic
def test_func(value):
    return value if value > 0 else 0
    
my_list = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# new_list = [i if i > 0 else 0 for i in my_list]
new_list = [test_func(i) for i in my_list]
print(new_list)

import random
def get_weather_data():
    return random.randrange(90, 110)

too_hot = [temp for _ in range(20) 
           if (temp := get_weather_data()) >= 100]
print(too_hot)

matrix = [[i for i in range(4)] for _ in range(4)]
print(matrix)

my_list = [10, 34, 56, 1, 1, 2, 4, 3, 102, 102]
my_set = {i for i in my_list if i%2 == 0}
print(my_set)

my_dict = {i: i * i for i in range(10)}
print(my_dict)
