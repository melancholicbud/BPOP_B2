my_list = [1, 2, 3]
first_iter = iter(my_list)
second_iter = iter(my_list)
print(next(first_iter))
print(next(first_iter))
print(next(second_iter))
print(next(first_iter))
# StopIteration error
# print(next(first_iter))

first_iter = iter(my_list)
print(first_iter.__next__())