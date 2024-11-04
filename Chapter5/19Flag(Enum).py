from enum import Flag, auto

class BoolFlag(Flag):
    A = auto()
    B = auto()
    C = auto()
    D = auto()
    # combination flags can't be here
    E = (A|B|C)^D

if __name__ == "__main__":
    print(repr(BoolFlag.A | BoolFlag.B))
    print(repr(BoolFlag.D & BoolFlag.C))
    print(repr(BoolFlag.D ^ BoolFlag.C))

    print(repr(BoolFlag.E))