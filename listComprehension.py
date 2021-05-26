my_list = [num for num in range(0, 100)]
print(my_list)

# times 2

my_list3 = [num**2 for num in range(0, 100)]
print(my_list3)

my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]
print(my_list4)

# set Comprehension
my_list5 = {num**2 for num in range(0, 100)}
print(my_list5)


my_dict = {num: num*2 for num in [1, 2, 3]}
print(my_dict)
