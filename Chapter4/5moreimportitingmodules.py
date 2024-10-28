# from import a, str1
import my_module1
a = my_module1.a
str1 = my_module1.str1
del my_module1

# some example which will be refactored below
# first.py
def function():
    print('first')

# second.py
def function():
    print('second')

# main.py
import first
import second

if __name__ == "__main__":
    first.function()
    second.function()

# refactored code from above
# main.py
from first import function
from second import function
# from second rewrites function name, ejected from first
if __name__ == "__main__":
    function()

# there is outcome from one more problem above
# main.py
from first import function as ffunction
from second import function as sfunction
if __name__ == "__main__":
    ffunction() # first 
    sfunction() # second