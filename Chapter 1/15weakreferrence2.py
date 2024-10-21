import weakref
class MyList(list):
    pass

my_list = MyList(range(10))
print(my_list)
ref_list = weakref.ref(my_list)
print(ref_list())

new_list = list(range(10))
# special error: TypeError
ref_new_list = weakref.ref(new_list)