import sys
one = two = three = object()
print(sys.getrefcount(one))
three = 4
print(sys.getrefcount(one))