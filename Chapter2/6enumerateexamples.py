my_str = 'Test'
index = 0
for it in my_str:
    print('Index of element ',it,' = ', index)
    index += 1

for index, it in enumerate(my_str):
    print('Index of element ',it, ' = ', index)

test = enumerate(my_str)
print(next(test))
print(next(test))
print(next(test))
print(next(test))
