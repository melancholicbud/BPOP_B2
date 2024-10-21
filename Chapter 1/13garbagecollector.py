import ctypes
import gc

if __name__ == '__main__':
    # using for access to object via address in memory
    class PyObject(ctypes.Structure):
        _fields_ = [("refcnt", ctypes.c_long)]
    gc.disable() # turning off GC

    my_list = []
    my_list.append(my_list)
    my_list_address = id(my_list)
    del my_list

    first_dict = {}
    second_dict = {}
    first_dict['second'] = second_dict
    second_dict['first'] = first_dict
    my_dict_address = id(first_dict)
    del first_dict, second_dict
    # gc.collect() # turning on manually
    # checking amount of pointers
    print(f'Amount of pointers for the list = '
          f'{PyObject.from_address(my_list_address).refcnt}')
    print(f'Amount of pointers for the dict = '
          f'{PyObject.from_address(my_dict_address).refcnt}')
