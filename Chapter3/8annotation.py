def sum_ab1(a: int, b: float) -> float:
    return a+b
print(sum_ab1.__annotations__)
for arg in sum_ab1.__annotations__:
    print(arg, '=>', sum_ab1.__annotations__[arg])

def sum_ab2(a: 'what?', b: 99, c) -> 'h.. holy python!!!':
    return a+b
print(sum_ab2.__annotations__)
for arg in sum_ab2.__annotations__:
    print(arg, '=>', sum_ab2.__annotations__[arg])

def sum_ab3(a: 'what?' = 2, b: (4, 5)=99, c: float=3.5) -> 'h.. holy python!!!':
    return a+b
print(sum_ab3.__annotations__)
for arg in sum_ab3.__annotations__:
    print(arg, '=>', sum_ab3.__annotations__[arg])
print(sum_ab3())
print(sum_ab3(1, 3))
print(sum_ab3(c=-5))
