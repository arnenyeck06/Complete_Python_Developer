
# # Decorator pattern


# def my_decorator(func):
#     def wrap_func(y, a):
#         print('**********')
#         func(y, a)
#         print('**********')
#     return wrap_func


# @my_decorator
# def hello(greeting, emoji):
#     print(greeting, emoji)


# hello('salut', ':)')

from time import time


def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'It took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000):
        i*5


long_time()
