from private_names import *

if __name__ == "__main__":
    function(20)
    # NameError
    # _internal_func(20)
    print(first)
    # NameError
    # print(_second)

import private_names
if __name__ == "__main__":
    private_names._internal_func(20)
    print(private_names._second)
    