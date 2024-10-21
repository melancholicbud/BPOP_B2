import weakref
class TestWeakRef:
    def say(self, name="NoName"):
        print(f'Hi, {name}!')

strong_ref = TestWeakRef()
weak_ref = weakref.ref(strong_ref)
weak_ref().say()
weak_ref().say('Alex')
print(weak_ref() is strong_ref)
del strong_ref
print(weak_ref())