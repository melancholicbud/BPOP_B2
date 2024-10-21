import sys
x = 15 # value in bytes?
print(sys.getsizeof(x))
y = 15
print (x is y)
print(sys.getsizeof(object()))