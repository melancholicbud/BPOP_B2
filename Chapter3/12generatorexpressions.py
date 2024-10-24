print([x+2 for x in range(5)])
print((x+2 for x in range(5)))

# we can rewrite it
"""
def gen_func(N):
    for it in range(N):
        yield '-_-'
func_iter = gen_func(4)
for it in func_iter:
    print(it)
"""
new_func_iter = ('-_-' for _ in range(4))
for it in new_func_iter:
    print(it)

# or

for it in ('-_-' for _ in range(4)):
    print(it)

# adding filtration by parity
for it in ('-_-' for x in range(4) if x % 2 == 0):
    print(it)