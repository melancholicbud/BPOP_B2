my_str = 'Test'
# we can initialize variable with double quotes
# my_str = "Test"
print(len(my_str))
print(my_str[0])
# we output the first element my_str,
# because indexing starts with 0
print(my_str[-1])
print(my_str[-3])

print(my_str[1:3])
# cut my_str from offset 1 to 2 inclusive (not 3)

# full string
print(my_str[:])
# everything after the first element
print(my_str[1:])
# except the last element
print(my_str[0:3])
# the same that my_str[0:3]
print(my_str[:3])
# the same as previous line
print(my_str[:-1])

# from first to the last element with step 1\
print(my_str[::1])
# with step 2
print(my_str[::2])
# the analogue of previous line
print(my_str[0:4:2])
# from second to the last element with step 2
print(my_str[1::2])
# reverse the line
print(my_str[::-1])

# concatenation (my_str won't change)
print(my_str+'Ko')
# repetition (my_str won't change)
print(my_str * 3)
# concatenation
print([1, 2, 3] + [4, 5])
# repetition
print([1, 2, 3] * 3)

# special error: TypeError
# my_str[1] = 'E'

# but we can create a new objects
my_str = my_str[1:] + 'E'
print(my_str)

# let's modify
my_str = 'Test'
# reverse in list
my_list = list(my_str)
print(my_list)
my_list[0] = 'F' # changing
# joining with empty symbol
print(''.join(my_list))

# hybrid bytes/lists
my_array = bytearray(b'Test')
my_array.extend(b'Ko')
print(my_array)
# decoding in normal string
print(my_array.decode())

# searching substring offset in my_str
print(my_str.find('es'))
# replacing the occurrence of a substring in my_str with another
print(my_str.replace('es', ' XFQ'))
print(my_str)

line = 'ffff, tt, nn, d'
# cut string with coma in substring list
print(line.split(','))

# uppercase
print(my_str.upper())
line = 'ffff,ttt,nn,d\n'
# deleting \n
print(line.rstrip())

# changing substring in string with cutting in list
print(line.replace('tt', 'XFQ').split(','))
