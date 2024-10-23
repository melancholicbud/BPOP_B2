def connet_stud_with_test(st_dict, ts_dict):
    bd_table = {}
    print("Connection of student's id with id variants: ")
    var_amount = len(ts_dict.keys())
    current_var = list(ts_dict.keys())[0]
    for id_stud in st_dict.keys():
        bd_table[id_stud] = current_var % var_amount
        current_var += 1
        print(id_stud, bd_table[id_stud])
    print("\n\n")
    return bd_table

x = 3
y = 5
if x > y:
    print("x > y")
    print(x - y)
else:
    print("y >= x")
    print(y - x)
