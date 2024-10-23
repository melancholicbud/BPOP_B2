first_list = [1, 2, 3, 4, 5]
second_list = [6, 7, 8, 9, 10]
print(list(zip(first_list, second_list)))

for a, b in zip(first_list, second_list):
    print(a, '+', b, '=', a+b)

one, two, three = (1,2,3), (4,5,6), (7,8,9)
print(list(zip(one, two, three)))
for a, b, c in zip(one, two, three):
    print('({} - {}) * {} = {}'.format(b, a, c, (b-a)*c))

one, two, three = (1,2,3,5,9), (4,5,6), (7,8,9,23)
print(list(zip(one, two, three)))