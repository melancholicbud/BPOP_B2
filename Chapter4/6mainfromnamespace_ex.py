import namespaces_ex

if __name__ == "__main__":
    pass

if __name__ == "__main__":
    attr_key = namespaces_ex.__dict__.keys()
    print(list(attr_key))
    attr_key = [name for name in attr_key if not name.startswith('__')]
    print(attr_key)

    print(namespaces_ex.name_a)
    print(namespaces_ex.__dict__['name_a'])
    

