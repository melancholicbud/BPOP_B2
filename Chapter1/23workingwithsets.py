mylist = [0, 1, 1, 2, 3, 9, 3, 4, 5, 6, 6, 7, 8, 9]
my_set = set()
my_set = set(mylist)
my_set = {0, 1, 1, 2, 3, 9, 4, 5, 6, 6, 7, 8, 9}
print(my_set)

my_set.add(102)
print(my_set)

my_set.update([2, 100, 99, 4, 5, 6])
# or my_set.update({2, 100, 99, 4, 5, 6})
print(my_set)

my_set.remove(2)
print(my_set)
my_set.discard(100)
print(my_set)

my_set.remove(2)
# keyerror
# print(my_set)

A = {0, 1, 1, 2, 3, 9, 4, 5, 6, 6, 7, 8, 9}
B = {1, 3, 6, 10, 15, 21, 28, 36, 45}
# union
new_set = A | B
print(new_set)
# intersection
new_set = A & B
print(new_set)
# symmetric difference
new_set = A ^ B
print(new_set)
# difference 
new_set = A - B
print(new_set)
new_set = B - A
print(new_set)

# 3 operations are symmetrical
check = (A | B) == (B | A)
print(check)
check = (A & B) == (B & A)
print(check)
check = (A ^ B) == (B ^ A)
print(check)
check = (A - B) == (B - A)
print(check)

# is subset or superset
A = {1, 2, 3}
B = {1, 2, 3, 4}
print(A.issubset(B))
print(B.issuperset(A))
A.add(5)
print(A.issubset(B))
print(B.issuperset(A))

B = {1, 2, 3, 4}
print(0 in B)
print(1 in B)
print(0 not in B)
print(1 not in B)
