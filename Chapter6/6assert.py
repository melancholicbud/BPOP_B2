def test_assert(value):
    assert value > 0, 'value must be > 0'
    return 30/value

if __name__ == "__main__":
    print(test_assert(10))
    print(test_assert(0))