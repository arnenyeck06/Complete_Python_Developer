from functools import reduce
import math

my_list = [1, 2, 3]


def multiply_by2(item):
    return item*2


print(list(map(lambda item: item*2, my_list)))


# def multiply_by2(item):
#     return item*2  still works without this.

# Create a lamba expression that will square the list
mylist = [5, 4, 3]

print(list(map(lambda item: item ** 2, mylist)))

# SORTING LIST
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda x: x[1])
print(a)
