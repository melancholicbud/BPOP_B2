"""while True: 
    print("I'm invisible")
"""

x = 0
y = 5
while x < y:
    print(x, end=' ')
    x += 1

x = 0
y = 5
while x < y:
    print(x, end=' ')
    x += 1
else:
    print('Happy End!')

x = 0
y = 5
while x < y:
    print(x, end=' ')
    x += 1
    if x > y-2: break
else:
    print('Happy End!')

# pass
while True: pass
def test():
    pass

# continue
a = 15
while a:
    x = a - 1 # a -= 1
    if a % 2 != 0: 
        continue
    print(a, end=' ')


# break
my_sum = 0
while True:
    val = int(input('Input int: '))
    if val == 0: break
    my_sum += val
    print('Current sum: ', my_sum)
print('Total sum: ', my_sum)