# # my_list = [1, 2, 3]


# # def multiply_by2(item):
# #     return item*2


# # print(list(map(multiply_by2, [1, 2, 3])))
# # print(my_list)


# # # FILTER
# # def check_odd(item):
# #     return item % 2 != 0


# # print(list(filter(check_odd, [1, 2, 3])))
# # print(my_list)


# # ZIP

# from functools import reduce
# my_list = [1, 2, 3]

# your_list = [10, 20, 30]


# def multiply_by2(item):
#     return item*2


# print(list(map(multiply_by2, [1, 2, 3])))
# print(my_list)


# # FILTER
# def check_odd(item):
#     return item % 2 != 0


# print(list(zip(my_list(your_list))))


# REDUCE
from functools import reduce
my_list2 = [2, 3, 4]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(3, 3)
    return acc + item


print(reduce(accumulator, my_list2, 0))
print(my_list2)
