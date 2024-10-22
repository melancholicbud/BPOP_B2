str1 = "Itsfantastic"
str2 = "Itsfantastic"
print(f'S1id = {id(str1)}; S2 = {id(str2)}')
print(str1 is str2)

str2 = "Its fantastic"
print(f'S1id = {id(str1)}; S2 = {id(str2)}')
print(str1 is str2)

import sys
str1 = sys.intern("It's fantastic!")
str2 = sys.intern("It's fantastic!")
print(f'S1id = {id(str1)}; S2 = {id(str2)}')
print(str1 is str2)

str1 = sys.intern("It's fantastic!")
str2 = "It's fantastic!"
print(f'S1id = {id(str1)}; S2 = {id(str2)}')
print(str1 is str2)