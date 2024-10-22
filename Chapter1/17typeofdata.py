n = 10
b = n
print('id n = ', id(n))
print('id b = ', id(b))

n = 5
print('id n = ', id(n))
print('id b = ', id(b))

n = [1, 2]
b = n
print('id n = ', id(n))
print('id b = ', id(b))

b[0] = 5
b[1] = 4
print('id n = ', id(n))
print('id b = ', id(b))

from typing import List, Dict
n : int = 4
b : float = 3.5
myList : List[int] = [1, 3, 4]
myDict : Dict[str, float] = {'sd' : 3.4, 'rd1' : 4.76}
