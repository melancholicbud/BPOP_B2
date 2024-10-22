myfile = open('myfile.txt', 'w')
myfile.write('There is something I want to tell you..\n')
myfile.write('Well, I made it, friend.\n')
myfile.close()
myfile = open('myfile.txt', 'r')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
# reading everything in file
print(open('myfile.txt', 'r').read())

myfile = open('myfile.txt', 'r')
for line in myfile:
    print(line, end='')

a, b, c = 43, 23, 45
mytext = 'Test'
mydict = {'a' : 1, 'b' : 2}
mylist = [1, 2, 3]
myfile = open('datafile.txt', 'w')
myfile.write(mytext + '\n')
# convert ints in strings
myfile.write('%s, %s, %s\n' % (a, b, c))
# convert and cutting by $ sign
myfile.write(str(mylist ) + '$' + str(mydict) + '\n')
myfile.close()

print(open('datafile.txt', 'r').read())

myfile = open('datafile.txt', 'r')
mytext = myfile.readline()
# deleting a symbol end of the string
mytext = mytext.rstrip()
print(mytext)
my_numbers_str = myfile.readline()
# cutting by commas
my_numbers_str = my_numbers_str.split(',')
# just see
my_numbers = [int(it) for it in my_numbers_str]
print(my_numbers)

mydict_and_list = myfile.readline().split('$')
print(mydict_and_list)
print(eval(mydict_and_list[1]))
objects = [eval(P) for P in mydict_and_list]
print(objects)
myfile.close()

import pickle
mydict = {'a' : 1, 'b' : 2}
myfile = open('datafile.pkl', 'wb')
pickle.dump(mydict, myfile)
myfile.close()

myfile = open('datafile.pkl', 'rb')
mydict = pickle.load(myfile)
print(mydict)
myfile.close()

import json
name = dict(first='John', last='Johnson')
my_dict = dict(name=name, job=['developer', 'student'], age=21.5)
print(my_dict)
json.dump(my_dict, fp=open('testjson.txt', 'w'), indent=4)
my_json_obj = json.load(open('testjson.txt'))
print(my_json_obj)