import weakref
class TestWeakRef(object):
    def __del__(self):
        print('Class deleted!')

    def say(self, name="NoName"):
        print(f'Hi, {name}!')

def callback(ref):
    # Invoked when referenced object is deleted
    print("I'am free!!!!")

strong_ref = TestWeakRef()
weak_ref = weakref.ref(strong_ref, callback)
weak_ref().say()
weak_ref().say('Alex')
del strong_ref
print('weak_ref(): ', weak_ref())
