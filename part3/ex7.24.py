from registration_param import *


if __name__ == '__main__':
    print(registry)
    print(register()(f3))
    print(registry)
    print(register(active=False)(f2))
    print(registry)
