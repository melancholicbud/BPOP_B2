def maker1(N):
    def action(X): # creating and returning 'action' function
        return X ** N
    return action

my_func = maker1(3)
print(my_func(2))
print(my_func(4))
print(my_func(5))

def maker2(N):
    return lambda X: X ** N
my_func = maker2(3)
print(my_func(2))
print(my_func(4))
print(my_func(5))


def counter1(start):
    state = start
    def adder1(X):
        print(X + state)
    return adder1
F = counter1(5)
F(3)
F(5)

# special error: UnboundLocalError
# for see that error - comment 'nonlocal state' line
def counter2(start):
    state = start
    def adder2(X):
        # state = start # uncomment & clean this line above to see SyntaxError
        nonlocal state
        print(X + state)
        state += 1
    return adder2
F = counter2(0)
F(3)

# more SyntaxError
"""
state = 10
def counter3():
    def adder3(X):
        nonlocal state
        print(X + state)
        state += 1
    return adder3
F = counter()
"""

