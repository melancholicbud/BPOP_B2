print(range(10))
print(list(range(10)))

print(range(0,6))
print(list(range(0, 6)))

print(range(0, 6, 2))
print(list(range(0, 6, 2)))

print(list(range(-5, 5)))
print(list(range(5, -5, -1)))

for i in range(3):
    print(i, 'Test')

my_str = 'Test'
for it in my_str:
    print(it, end=' ')
print(len(my_str))
print(list(range(len(my_str))))
# manual iteration via range/len
for it in range(len(my_str)):
    print(my_str[it], end=' ')