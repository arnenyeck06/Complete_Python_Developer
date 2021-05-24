def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([2, 4, 6]))  # no interaction with the outside world.

# new_list = [] # new list is outside of the world, making the loop interacting with
# the outside, so not a pure func.

# def multiply_by2(li):

#     for item in li:
#         new_list.append(item*2)
#     return new_list


# print(multiply_by2([2, 4, 6]))
