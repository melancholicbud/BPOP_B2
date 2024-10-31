# overloading __add__, __or__, __sub__
class Number:
    def __init__(self, val):
        self.value = val
    
    def __sub__(self, other):
        return Number(self.value - other)
    
    def __add__(self, other):
        return Number(self.value + other)
    
    def __or__(self, other):
        return Number(self.value | other)
    
    def __str__(self):
        return f'{self.value}'
    

if __name__ == "__main__":
    my_number = Number(4)
    addValue = my_number + 10
    print(addValue)
    subValue = addValue - 13
    print(subValue)
    orValue = subValue | 4
    print(orValue)


# overloading __getitem__ & __setitem__
class CustomList:
    def __init__(self, elements_amount=1):
        self.__custom_list = [0] * elements_amount
        self.size = elements_amount

    def __str__(self):
        return f'{self.__custom_list}'
    
    def __getitem__(self, item):
        if not self.__index_check(item):
            new_list = CustomList(self.size)
            new_list.__custom_list = self.__custom_list[item]
            return new_list
        return self.__custom_list[item]
    
    def __setitem__(self, key, value):
        if self.__index_check(key):
            self.__custom_list[key] = value
        else:
            my_range = range(key.start if key.start else 0, key.stop,
                             key.step if key.step else 1)
            for it in my_range:
                self.__custom_list[it] = value
    
    def __index_check(self, index):
        if isinstance(index, int):
            print(f'current index = {index}')
            return True
        elif isinstance(index, slice):
            print(f'slice: start = {index.start}',
                  f'stop = {index.stop}',
                  f'step = {index.step}')
            return False
        else:
            raise IndexError("Bad Index")

if __name__ == "__main__":
    my_list = CustomList(8)
    print(my_list)
    my_list[4] = 35
    print(my_list)
    my_list[0:4] = 50
    print(my_list)
    new_list = my_list[0:6:2]
    print(new_list)
    # IndexError
    # my_list['2']


# __iter__ & __next__
class MyRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.count_value = 0
    
    def __iter__(self):
        self.count_value = self.start - self.step
        return self
    
    def __next__(self):
        if self.count_value+self.step >= self.stop:
            raise StopIteration
        self.count_value += self.step
        return self.count_value
    
if __name__ == "__main__":
    my_range = MyRange(0, 4)
    for it in my_range:
        print(it, end=' ')
    print()
    for it in MyRange(0, 12, 4):
        print(it, end=' ')
    my_iter = iter(my_range)
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    # StopIteration
    # print(next(my_iter))

class MyGeneratorRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        count_value = self.start - self.step
        while count_value+self.step < self.stop:
            count_value += self.step
            yield count_value

if __name__ == "__main__":
    print("MyGeneratorRange")
    my_range = MyGeneratorRange(0, 4)
    for it in my_range:
        print(it, end=' ')
    print()
    for it in MyGeneratorRange(0, 12, 4):
        print(it, end=' ')

    my_iter = iter(my_range)
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    # StopIteration
    # print(next(my_iter))

    test_range = MyRange(0, 3)
    for first_it in test_range:
        print(first_it)
        for second_it in test_range:
            print(f'second_it = {second_it}, ' 
                  f'first_it*second_it = {first_it*second_it}')
            
    test_range = MyGeneratorRange(0, 3)
    for first_it in test_range:
        print(first_it)
        for second_it in test_range:
            print(f'second_it = {second_it}, ' 
                  f'first_it*second_it = {first_it*second_it}')
    