"""ex. 1: characters at even indices"""
"""ex. 2: characters at indices divisible by 3 but not 4"""
"""ex. 3: characters at indices giving remainders 2, 4, 5 when divided by 6"""
string = "This part focused more on Python syntax and code documentation issues."
# ex. 1
result = [char for index, char in enumerate(string) 
          if index % 2 == 0]
print("".join(result))
# ex. 2
result = [char for index, char in enumerate(string) 
          if index % 3 == 0 and index % 4 != 0]
print("".join(result))
# ex. 3
result = [char for index, char in enumerate(string) 
          if index % 6 in (2, 4, 5)]
print("".join(result))

"""ex. 4: numbers from 1 to 10 (using for and while)"""
# for loop
for i in range(1, 11):
    print(i, end=" ")
print()

# while loop
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

"""ex. 5: numbers from -20 to 20 with step 3"""
# for loop
for i in range(-20, 21, 3):
    print(i, end=" ")
print()

# while loop
i = -20
while i <= 20:
    print(i, end=" ")
    i += 3
print()

"""ex. 6: count occurrences of '3' in the list"""
lst = [3, 0, 1, 3, 0, 4, 3, 3, 4, 5, 6, 6, 1, 3]

# Using for loop
count_for = 0
for num in lst:
    if num == 3:
        count_for += 1
print("Count using for:", count_for)

# Using while loop
count_while = 0
i = 0
while i < len(lst):
    if lst[i] == 3:
        count_while += 1
    i += 1
print("Count using while:", count_while)

# Using count method
print("Count using count method:", lst.count(3))


"""ex. 7: create list from string using list comprehension"""
string = "list of available attributes"
lst = [char for char in string]
print(lst)

"""ex. 8: create identity matrix using list comprehensions"""
N = 3 # size of matrix
identity_matrix = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
for row in identity_matrix:
    print(row)

"""ex. 9: reverse list elements"""
lst = [3, 0, 1, 3, 0, 4, 3, 3, 4, 5, 6, 6, 1, 3]
reversed_lst = lst[::-1]
print(reversed_lst)

"""ex. 10: numbers from 1 to 9 excluding 5 and 7"""
for i in range(1, 10):
    if i not in (5, 7):
        print(i, end=" ")
print()

"""ex. 11: sum of list elements using for, while and sum"""
# for loop
sum_for = 0
for num in lst:
    sum_for += num
print("Sum using for:", sum_for)
# while loop
sum_while = 0
i = 0
while i < len(lst):
    sum_while += lst[i]
    i += 1
print("Sum using while:", sum_while)
# sum
print("Sum using sum method:", sum(lst))

"""ex. 12: sum of elements at indices divisible by 3"""
# for loop
sum_for = 0
for index, value in enumerate(lst):
    if index % 3 == 0:
        sum_for += value
print("Sum using for:", sum_for)
# while loop
sum_while = 0
i = 0
while i < len(lst):
    if i % 3 == 0:
        sum_while += lst[i]
    i += 1
print("Sum using while:", sum_while)

"""ex. 13: list of elements in range 23 to 35"""
lst = list(range(23, 36))
print(lst)

"""ex. 14: list of elements from 3 to 15 with step 4"""
lst = list(range(3, 16, 4))
print(lst)

"""ex. 15: list of elements from 3 to 25 divisible by 3"""
lst = [x for x in range(3, 26) if x % 3 == 0]
print(lst)

"""ex. 16: dictionary from two lists using zip"""
keys = [3, 0, 1, 3, 0, 4, 3, 3, 4, 5, 6, 6, 1, 3]
values = [2, 4, 7, 26, 33]
dictionary = dict(zip(keys, values))
print(dictionary)

"""ex. 17: print list elements with their indices"""
lst = [3, 0, 1, 3, 0, 4, 3, 3, 4, 5, 6, 6, 1, 3]
# for loop with enumerate
for index, value in enumerate(lst):
    print(f"Index {index}: {value}")
# for loop without enumerate
for i in range(len(lst)):
    print(f"Index {i}: {lst[i]}")

"""ex. 18: program to identify season by month"""
month = int(input("Enter the month number (1-12): "))
if month in (12, 1, 2):
    print("Winter")
elif month in (3, 4, 5):
    print("Sprint")
elif month in (6, 7, 8):
    print("Summer")
elif month in (9, 10, 11):
    print("Autumn")
else:
    print("Invalid month number")

"""ex. 19: program to print average of three values"""
a, b, c = 5, 10, 15
average = (a + b + c) / 3
print("Average: ", average)

"""ex. 20: multiplication table for user-provided number"""
num = int(input("Enter a number (1-9): "))
for i in range(1, 10):
    print(f"{num} x {i} = {num * i}")
