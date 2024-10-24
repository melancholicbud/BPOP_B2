"""ex. 1: function to find the maximum of three numbers"""
def max_of_three(a, b, c):
    return max(a, b, c)


"""ex. 2: function to return the sum of a list's elements:"""
def sum_of_list(lst):
    return sum(lst)

"""ex. 3: function to return the product of a list's elements"""
def product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

"""ex. 4: function to return the reversed string"""
def reverse_string(s):
    return s[::-1]

"""ex. 5: function to compute the factorial of a number"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
"""ex. 6: function to check if a value is in a specified range"""
def is_in_range(value, start, end):
    return start <= value <= end

"""ex. 7: function to count the number of lowercase and uppercase characters"""
def count_case(s):
    lower_count = sum(1 for c in s if c.islower())
    upper_count = sum(1 for c in s if c.isupper())
    return lower_count, upper_count

"""ex. 8: function to remove duplicates from a list"""
def remove_duplicates(lst):
    return list(set(lst))

"""ex. 9: function to print elements of a list with even indices"""
def print_even_index_elements(lst):
    for i in range(0, len(lst), 2):
        print(lst[i])

"""ex. 10: function to check if a string is a palindrome"""
def is_palindrome(s):
    return s == s[::-1]

"""ex. 11: decorator to wrap return string value in <b></b>"""
def bold_decorator(func):
    def wrapper1(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper1

"""ex. 12: decorate a function to square the return value"""
def square_decorator(func):
    def wrapper2(*args, **kwargs):
        result = func(*args, **kwargs)
        return result ** 2
    return wrapper2

"""ex. 13: decorate a function to return string in uppercase"""
def uppercase_decorator(func):
    def wrapper3(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper3

"""ex. 14: decorator to print input arguments of a function"""
def print_args_decorator(func):
    def wrapper4(*args, **kwargs):
        print("Arguments: ", args, kwargs)
        return func(*args, **kwargs)
    return wrapper4

"""ex. 15: generator function to iterate values from 23 to 37"""
def generate_range():
    for i in range (23, 38):
        yield i

"""ex. 16: generator function to iterate values from 5 to 37 with a step of 4"""
def generate_range_with_step():
    for i in range(5, 38, 4):
        yield i

"""ex. 17: generator expression to iterate from 0 to 15"""
gen_expr = (x for x in range(16))

"""ex. 18: generator expression to iterate through the list and square elements"""
lst = [3, 0, 1, 3, 0, 4, 3, 3, 4, 5, 6, 6, 1, 3]
gen_square = (x ** 2 for x in lst)

"""ex. 19: generator function with adjustable step"""
def adjustable_step_generator(step):
    i = 0
    while i < 100:
        yield i
        i += step

"""ex. 20: create a list using the generator functions"""
list1 = list(generate_range())
list2 = list(generate_range_with_step())
final_list = list1 + list2