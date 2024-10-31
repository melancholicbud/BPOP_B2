class MyRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        return MyRangeIterator(self)

class MyRangeIterator:
    def __init__(self, myrange_object):
        self.my_range = myrange_object
        self.count_value = myrange_object.start - myrange_object.step

    def __next__(self):
        if self.count_value+self.my_range.step >= self.my_range.stop:
            raise StopIteration
        self.count_value += self.my_range.step
        return self.count_value
    
if __name__ == "__main__":
    print("MyRange")
    my_range = MyRange(0, 4)
    for it in my_range:
        print(it, end=' ')
    print()
    for it in MyRange(0, 12, 4):
        print(it, end=' ')
    test_range = MyRange(0, 3)
    for first_it in test_range:
        print(first_it)
        for second_it in test_range:
            print(f'second_it = {second_it}, ' 
                  f'first_it*second_it = {first_it*second_it}')

# __contains__
class TestContains:
    def __init__(self, value):
        self.data = value
    
    def __contains__(self, x):
        return x in self.data
    
if __name__ == '__main__':
    X = TestContains([1, 2, 3, 4, 5])
    print(3 in X)
    print(10 in X)
    print('d' in X)

# __ getattr__ & __setattr__
class TestAttribute:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        print("in __getattr__")
        if item == "age":
            self.__dict__[item] = 3
            return self.__dict__[item]
        else:
            raise AttributeError(item)
    
    def __setattr__(self, key, value):
        print(f"in __setattr__, key = {key}, value = {value}")
        if key == "age":
            self.__dict__[key] = value + 1
        elif key == "name":
            self.__dict__[key] = value
        else:
            raise AttributeError(value + " not allowed")
        
if __name__ == "__main__":
    my_test = TestAttribute("Alex")
    print(my_test.name)
    print(my_test.age)
    print(my_test.age)
    # AttributeError
    # print(my_test.country)
    my_test.name = "John"
    my_test.age = 10
    print(my_test.name)
    print(my_test.age)
    # AttributeError
    # my_test.country = "Germany"

# more example
class PrivateExc(Exception):
    pass

class PrivateAttribute:
    def __setattr__(self, key, value):
        print(f"check key = {key}, value = {value}")
        if key in self.privates:
            raise PrivateExc(key, self)
        else:
            self.__dict__[key] = value

class FirstTestAttribute(PrivateAttribute):
    privates = ["name", "city"]

class SecondTestAttribute(PrivateAttribute):
    privates = ["age"]

    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    first_test = FirstTestAttribute()
    second_test = SecondTestAttribute("Alex")
    second_test.city = "Hamburg"
    first_test.country = "Germany"
    # first_test.name = "John"


# __repr__ & __str__
class Number:
    def __init__(self, val):
        self.value = val
    
    def __sub__(self, other):
        return self.value - other

if __name__ == "__main__":
    number = Number(10)
    print(number)

class NewNumber(Number):
    def __repr__(self):
        return f'{self.value}'

if __name__ == "__main__":
    newNumber = NewNumber(15)
    print(newNumber)
    newNumber = newNumber - 3
    print(newNumber)


# __call__
class CallTest:
    def __call__(self, *args, **kwargs):
        print("__call__")
        print(f"args = {args} \nkwargs = {kwargs}")

if __name__ == "__main__":
    test = CallTest()
    test(10, 'Oo', 32.1)
    test(10, 'Oo', 32.1, a=2, b='-_-')

class CallTest2:
    def __call__(self, a, b, c=3):
        print("__call__")
        print(f"a = {a}, b = {b}, c = {c}")

if __name__ == "__main__":
    test2 = CallTest2()
    test2(4, '^_^')
    test2(b=4, c=45.3, a='^_^')
    # TypeError
    # test2(8)

class Person:
    def __init__(self, name="Nazar"):
        self.name = name
    
    def __call__(self, profession):
        print(f"{self.name} is a {profession}")

class ProfessionName:
    def __init__(self, person, prof="unemployed"):
        self.person = person
        self.profession = prof

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        if key == "profession":
            self.person(self.__dict__[key])

if __name__ == "__main__":
    person = Person("Alex")
    prof = ProfessionName(person)
    prof.profession = "doctor"
    prof.profession = "student"
