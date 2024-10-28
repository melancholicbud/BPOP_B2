# combined all along
from combined_operations import add, area_circle, is_palindrome, contains_element
from internal_names import get_value1, get_value2 # type: ignore

# Test arithmetic functions
print("Addition:", add(5, 7))

# Test area calculation
print("Circle Area:", area_circle(5))

# Test string functions
print("Is Palindrome:", is_palindrome("madam"))

# Test list functions
print("Contains Element:", contains_element([1, 2, 3, 4], 3))

# Test internal names
print("Value 1:", get_value1())
print("Value 2:", get_value2())