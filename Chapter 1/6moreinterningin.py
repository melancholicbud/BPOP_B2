x = 320
y = 320
print(f'Xid = {id(x)}; Yid = {id(y)}')
print(x is y)

x = 25
y = 24
print(f'Xid = {id(x)}; Yid = {id(y)}')
print(x is y)

y += 1
print(f'Xid = {id(x)}; Yid = {id(y)}')
print(x is y)

x = 540
y = 539
y += 1
print(f'Xid = {id(x)}; Yid = {id(y)}')
print(x is y)