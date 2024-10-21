my_list = [1, 3, 6]
my_list.append('Oo')
my_list[1] ='-_-'
bad_list = my_list
bad_list[0] = 5
bad_list.append(3.6)
# surface copying
bad_list = my_list.copy()