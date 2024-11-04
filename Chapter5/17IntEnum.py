from enum import IntEnum

class FirstEnum(IntEnum):
    GO = 1
    STOP = 2

class SecondEnum(IntEnum):
    TURN = 1
    DOWN = 2

if __name__ == "__main__":
    print(FirstEnum == 1)
    print(FirstEnum.GO == 1)
    print(FirstEnum.GO == SecondEnum.TURN)

from enum import Enum
class SecondEnum2(IntEnum):
    TURN = 1
    DOWN = 2

class Color(Enum):
    RED = 1
    BLACK = 2

if __name__ == "__main__":
    print(Color.RED == SecondEnum2.TURN)
    