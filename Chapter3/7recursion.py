def my_sum1(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + my_sum1(L[1:])
print(my_sum1([1, 2, 3, 4, 5, 20, 30]))

def my_sum2(L):
    return 0 if not L else L[0] + my_sum2(L[1:])
print(my_sum2([1, 2, 3, 4, 5, 20, 30]))

def my_sum3(L):
    return L[0] if len(L) == 1 else L[0] + my_sum3(L[1:])
print(my_sum3([1, 2, 3, 4, 5, 20, 30]))

def my_sum4(L):
    first, *rest = L
    return first if not rest else first + my_sum4(rest)
print(my_sum4([1, 2, 3, 4, 5, 20, 30]))

def my_sum5(L):
    if not L: return 0
    return nonempty(L)

def nonempty(L):
    return L[0] + my_sum5(L[1:])