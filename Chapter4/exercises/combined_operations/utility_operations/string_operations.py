# module for string operations
def is_palindrome(s):
    return s == s[::-1]

def string_length(s):
    return len(s)

def to_lowercase(s):
    return s.lower()