# <, >, >= etc.
class Number:
    def __init__(self, val):
        self.value = val
    
    def __lt__(self, other):
        return self.value < other
    
    def __gt__(self, other):
        return self.value > other
    
    def __le__(self, other):
        return self.value <= other
    
    def __ge__(self, other):
        return self.value >= other
    
    def __eq__(self, other):
        return self.value == other
    
    def __ne__(self, other):
        return self.value != other
    
if __name__ == "__main__":
    first = Number(10)
    second = Number(11)
    print(first < second)
    print(first > second)
    print(first <= second)
    print(first >= second)
    print(first == second)
    print(first != second)

# __len__ & __bool__
class MyTruth:
    def __bool__(self):
        return True
    
class MyTruth2:
    def __len__(self):
        return 0

class MyTruth3:
    def __bool__(self):
        return True
    
    def __len__(self):
        return 0
    
if __name__ == "__main__":
    my_truth = MyTruth()
    if my_truth:
        print("True")
    my_truth2 = MyTruth2()
    if not my_truth2:
        print("True")
    my_truth3 = MyTruth3()
    if my_truth3:
        print("True")

# @property etc.
class Person:
    def __init__(self, name="Alex", age=22):
        self.__person_name = name
        self.__person_age = age
    
    @property
    def name(self):
        print("get name", end=' ')
        return self.__person_name
    
    @property
    def age(self):
        print("get age", end=' ')
        return self.__person_age
    
    @age.setter
    def age(self, new_age):
        self.__person_age = new_age + 1
        print(f"set new age - {new_age}")
    
if __name__ == "__main__" :
    my_person = Person()
    print(my_person.name)
    print(my_person.age)
    my_person.name = "Maxim"
    my_person.age = 10
    my_person.name = 20