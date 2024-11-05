# ex. 1: Class for arithmetic operations with exception handling for null values
class ArithmeticOperations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        if self.a == 0 or self.b == 0:
            raise ValueError("One of the operands is zero.")
        return self.a + self.b

    def subtract(self):
        if self.a == 0 or self.b == 0:
            raise ValueError("One of the operands is zero.")
        return self.a - self.b

    def multiply(self):
        if self.a == 0 or self.b == 0:
            raise ValueError("One of the operands is zero.")
        return self.a * self.b

    def divide(self):
        if self.a == 0 or self.b == 0:
            raise ValueError("One of the operands is zero.")
        return self.a / self.b

# ex. 2: A class for division and multiplication with zero checking
class SafeOperations:
    def __init__(self, a, b):
        self.a = a if a != 0 else 1
        self.b = b if b != 0 else 1

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

# ex. 3:  Function for string conversion to uppercase with check for empty string
def to_uppercase(s):
    if not s:
        raise ValueError("String can't be empty")
    return s.upper()

# ex. 4:  Function to check if an element is included in the list with check for empty list
def element_in_list(element, lst):
    if not lst:
        raise ValueError("String can't be empty")
    return element in lst

# ex. 5: Custom exception class to check for the presence of the “p” character

class ContainsLetterPError(Exception):
    def __init__(self, message="The string contains the forbidden character 'h'"):
        self.message = message
        super().__init__(self.message)

def check_for_letter_p(s):
    if "h" in s:
        raise ContainsLetterPError()
    return s

if __name__ == "__main__":
# ex. 1: ArithmeticOperations
    def test1():
        try:
            ops = ArithmeticOperations(5, 0)
            print(ops.add())
        except ValueError as e:
            print(e)

# ex. 2
safe_ops = SafeOperations(0, 10)
print(safe_ops.multiply())  #  Multiplication will continue with the replacement of 0 by 1

# ex. 3
try:
    print(to_uppercase("hello"))
except ValueError as e:
    print(e)

# ex. 4: element_in_list
try:
    print(element_in_list(3, [1, 2, 3, 4]))
except ValueError as e:
    print(e)

# 6. check_for_letter_h
try:
    print(check_for_letter_p("hello"))
except ContainsLetterPError as e:
    print(e)
