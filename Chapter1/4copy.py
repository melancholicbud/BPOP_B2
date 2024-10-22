# surface copying
my_list = [2, 3 ,4, [1, 5]]
print(my_list)
bad_list = my_list.copy()
bad_list.append(10)
print(bad_list)
print(my_list)
bad_list[3].append('Oo')
print(bad_list)
print(my_list)

# deep copy
import copy
my_list = [2, 3 ,4, [1, 5]]
print(my_list)
bad_list = copy.deepcopy(my_list)
bad_list.append(10)
print(bad_list)
print(my_list)
bad_list[3].append('Oo')
print(bad_list)
print(my_list)