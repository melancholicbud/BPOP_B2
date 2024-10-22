""" ex. 1: length of string (two methods) """
string = "Hello, world!"
# len()
length1 = len(string)
# manual count
length2 = sum(1 for _ in string)
print("Length of the string: ", length1, "(Method 1)")
print("Length of the string: ", length2, "(Method 2)")

""" ex. 2: create new string from two first and two last characters"""
def create_new_string(s):
    return s[:2] + s[-2:] if len(s) >= 2 else ""

string = "Hello"
print(create_new_string(string))

"""ex. 3: replace character in string with $"""
string = "Hello, World!"
replaced = string.replace("o", "$")
print(replaced)

"""ex. 4: invert string sequence"""
string = "Hello, World!"
inverted = string[::-1]
print(inverted)

"""ex. 5: count occurrences of character in string"""
from collections import Counter
string = "google.com"
counter = Counter(string)
print(counter)

"""ex. 6: create two string from odd and even indices"""
string = "HelloWorld"
odd = string[1::2]
even = string[0::2]
print("Odd indices: ", odd)
print("Even indices: ", even)

"""ex. 7: remove specified character from string"""
string = "Hello, World!"
char_to_remove = "o"
result = string.replace(char_to_remove, "")
print(result)

"""ex. 8: convert string to upper and lower case"""
string = "Hello, World!"
print("Uppercase: ", string.upper())
print("Uppercase: ", string.lower())

"""ex. 9: display characters with their index"""
string = "Hello"
for index, char in enumerate(string):
    print(f"Index {index}: {char}")

"""ex. 10: check if character or word exists in string"""
string = "Hello, World!"
element = "world"
print(f"'{element}' in string: ", element in string)

"""ex. 11: most frequent character in string"""
from collections import Counter

string = "google.com"
most_common = Counter(string).most_common(1)[0]
print("Most frequent character: ", most_common)

"""ex. 12: swap case of string elements"""
string = "Hello, World!"
swapped = string.swapcase()
print(swapped)

"""ex. 13: sum elements in list (two ways)"""
numbers = [1, 2, 3, 4, 5]
# using sum()
sum1 = sum(numbers)
# using loop
sum2 = 0
for num in numbers:
    sum2 += num
print("Sum: ", sum1, "(Method 1)")
print("Sum: ", sum2, "(Method 2)")

"""ex. 14: multiply each list element by a number"""
numbers = [1, 2, 3, 4, 5]
multiplied = [num * 3 for num in numbers]
print(multiplied)

"""ex. 15: find maximum and minimum in list"""
numbers = [5, 2, 9, 1, 7]
print("Max: ", max(numbers))
print("Min: ", min(numbers))

"""ex. 16: remove duplicates from list"""
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print(unique)

"""ex. 17: copy list (two ways)"""
original = [1, 2, 3, 4, 5]
# copy()
copy1 = original.copy()
# slicing
copy2 = original[:]
print(copy1)
print(copy2)

"""ex. 18: concatenate two lists"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# using +
concatenated1 = list1 + list2
# extend()
list1.extend(list2)
print("Concatenated:", concatenated1)

"""ex. 19: swap elements at indices i and i+1"""
def swap_elements(lst, i):
    if i < len(lst) - 1:
        lst[i], lst[i + 1] = lst[i + 1], lst[i]

numbers = [1, 2, 3, 4]
swap_elements(numbers, 1)
print(numbers)

"""ex. 20: convert list of integers to single number"""
numbers = [15, 23, 150]
result = int("".join(map(str, numbers)))
print(result)

"""ex. 21: initialize dictionary (different ways)"""
# literal
dict1 = {"a": 1, "b": 2}
# dict()
dict2 = dict(c=3, d=4)
print(dict1)
print(dict2)

"""ex. 22: add pairs to dictionary"""
dictionary = {0: 10, 1: 20}
dictionary[2] = 30
dictionary[3] = 40
print(dictionary)

"""ex. 23: merge three dictionaries"""
dict1 = {1: "a"}
dict2 = {2: "b"}
dict3 = {3: "c"}
merged = {**dict1, **dict2, **dict3}
print(merged)

"""ex. 24: check if key exists in dictionary"""
dictionary = {"a": 1, "b": 2}
key = "a"
print(key in dictionary)

"""ex. 25: remove element from dictionary"""
dictionary = {"a": 1, "b": 2}
dictionary.pop("a", None)
print(dictionary)

"""ex. 26: maximum and minimum values in dictionary"""
dictionary = {"a" : 5, "b" : 2, "c" : 8}
print("Max: ", max(dictionary.values()))
print("Min: ", min(dictionary.values()))

"""ex. 27: initialize tuple and unpack"""
# initialize
tup = (1, 2, 3)
# unpack
a, b, c = tup
print(a, b, c)

"""ex. 28: add elements to tuple"""
tup = (1, 2, 3)
tup = tup + (4, 5)
print(tup)

"""ex. 29: convert list to tuple"""
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)

"""ex. 30: convert tuple to dictionary"""
tup = (("a", 1), ("b", 2))
dictionary = dict(tup)
print(dictionary)

"""ex. 31: count number of tuples in list"""
lst = [(1, 2,), (3, 4), "hello", 5]
count = sum(1 for item in lst if isinstance(item, tuple))
print(count)

"""ex. 32: initialize set (different ways)"""
# using {}
set1 = {1, 2, 3}
# set()
set2 = set([4, 5, 6])
print(set1)
print(set2)

"""ex. 33: add element to set"""
s = {1, 2, 3}
s.add(4)
print(s)

"""ex. 34: remove element from set"""
s = {1, 2, 3}
s.discard(2)
print(s)

"""ex. 35: remove duplicates from list (using set)"""
lst = [1, 1, 2, 3, 3, 4]
unique = list(set(lst))
print(unique)

"""ex. 36: union of two sets"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2
print(union)

"""ex. 37: length of set (two ways)"""
s = {1, 2, 3}
# len()
length1 = len(s)
# manual count
length2 = sum(1 for _ in s)
print(length1)
print(length2)

"""ex. 38: check if element in set"""
s = {1, 2, 3}
element = 2
print(element in s)

"""ex. 39: write text to file"""
with open("example.txt", "w") as file:
    file.write("Hello, World!")

"""ex. 40: read text from file"""
with open("example.txt", "r") as file:
    content = file.read()
print(content)

"""ex. 41: append text to file and display content"""
with open("example.txt", "a") as file:
    file.write("\nAppended text")
with open("example.txt", "r") as file:
    content = file.read()
print(content)

"""ex. 42: read last n lines from file"""
def read_last_lines(filename, n):
    with open(filename, "r") as file:
        lines = file.readlines()
        return lines[-n:]

print(read_last_lines("example.txt", 2))

"""ex. 43: count number of lines in file"""
with open("example.txt", "r") as file:
    line_count = sum(1 for _ in file)
print("Line count:", line_count)

"""ex. 44: most common word in file"""
with open("example.txt", "r") as file:
    words = file.read().split()
most_common_word = Counter(words).most_common(1)[0]
print("Most common word:", most_common_word)

"""ex. 45: copy contents from one file to another"""
with open("source.txt", "r") as source, open("destination.txt", "w") as dest:
    dest.write(source.read())

"""ex. 46: save dictionary using pickle"""
import pickle

dictionary = {"a": 1, "b": 2}
with open("dict.pkl", "wb") as file:
    pickle.dump(dictionary, file)

with open("dict.pkl", "rb") as file:
    loaded_dict = pickle.load(file)
print(loaded_dict)


"""ex. 47: save list using pickle"""
lst = [1, 2, 3]
with open("list.pkl", "wb") as file:
    pickle.dump(lst, file)

with open("list.pkl", "rb") as file:
    loaded_list = pickle.load(file)
print(loaded_list)

"""ex. 48: save dictionary using json"""
import json
dictionary = {"a": 1, "b": 2}
with open("dict.json", "w") as file:
    json.dump(dictionary, file)

with open("dict.json", "r") as file:
    loaded_dict = json.load(file)
print(loaded_dict)