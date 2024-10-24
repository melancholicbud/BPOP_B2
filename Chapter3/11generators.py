def gen_test():
    N = 0
    while N < 5:
        yield N
        N += 1

for x in gen_test():
    print(x, end=' ')

def gen_surprise_test():
    yield 0
    yield 1
    yield 2
    yield 3
    yield 4

for x in gen_surprise_test():
    print(x, end=' ')
iterator = gen_surprise_test()
print(iterator)
print(next(iterator))
print(iterator.__next__())
print(next(iterator))
print(next(iterator))
print(next(iterator))
# StopIterationError
# print(next(iterator))

def gen_send_test(N):
    for x in range(N):
        Y = yield x
        print(Y)

iterator = gen_send_test(2)
print(next(iterator))
print(iterator.send('-_-'))
# StopIteration
# print(iterator.send('o_o'))

def exept_gen_test(N):
    try:
        for x in range(N):
            yield x
    except GeneratorExit:
        print('EXCEPTION!!!')
    print('happy end!')

for it in exept_gen_test(30):
    if it >= 10:
        break
    print(it, end=' ')
    