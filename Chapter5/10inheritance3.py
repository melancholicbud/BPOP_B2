class BaseTextTest:
    name = "Test"

    def set_text(self):
        self.text = "Class BaseTextTest"
    
    def print_base(self): 
        return self.text

    def __str__(self):
        return self.text

class NewTextTest(BaseTextTest):
    def set_new_text(self):
        self.text = "Class NewTextTest"
    
    def print_new(self):
        return self.text
    
    def __str__(self):
        return self.text
    
if __name__ == "__main__":
    new_class = NewTextTest()
    new_class.set_text()
    print(new_class)
    print(new_class.print_base())
    print(new_class.print_new())
    new_class.set_new_text()
    print(new_class.print_new())
    print(new_class)

print(f'new_class = {new_class.name}',
      f' NewTextTest = {NewTextTest.name}',
      f'BaseTextTest = {BaseTextTest.name}')

NewTextTest.name = "Not bad"
print(f'new_class = {new_class.name}',
      f' NewTextTest = {NewTextTest.name}',
      f'BaseTextTest = {BaseTextTest.name}') 