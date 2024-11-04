from enum import Enum
class Color(Enum):
    BLACK = 0
    WHITE = 1
    RED = 2
    BLUE = 3

# TypeError
""" class TestEnum(Enum):
    ONE = 0
    ONE = 1 
"""

if __name__ == "__main__":
    print(Color.BLACK)
    print(Color.BLACK.name)
    print(Color.BLACK.value)

    for it in Color:
        print(it)

class TestNewEnum(Enum):
    ZERO = 0
    ONE = 1
    TWO = 0

if __name__ == "__main__":
    print(TestNewEnum.ZERO.value)
    print(TestNewEnum.ONE.value)
    print(TestNewEnum.TWO.value)

# for finding an error from above we need this:
from enum import Enum, unique
@unique
class TestNewEnum1(Enum):
    ZERO = 0
    ONE = 1
    TWO = 0

# or using auto:
from enum import Enum, auto

class TestNewEnum2(Enum):
    ZERO = auto()
    ONE = auto()
    TWO = auto()

if __name__ == "__main__":
    for it in TestNewEnum2:
        print(repr(it))

# if enum has written attributes, it can be base class while inheritance
class Color2(Enum):
    BLACK = 0
    WHITE = 1

# TypeError
"""
class NewColor(Color):
    GREEN = 99
"""

myColor = Enum('MyColor', 'BLACK WHITE RED BLUE')
for it in myColor:
    print(repr(it))

print(myColor.BLACK is myColor.BLACK)
print(myColor.BLACK is myColor.WHITE)
print(myColor.BLACK is not myColor.WHITE) 
print(myColor.BLACK == myColor.BLACK)
print(myColor.BLACK != myColor.WHITE) 
print(myColor.BLACK == myColor.WHITE)
print(myColor.BLACK == 1)