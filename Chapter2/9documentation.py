print(dir())
print(dir(dict))
print(len(dir({})))

print([it for it in dir(dict) if not it.startswith('__')])

