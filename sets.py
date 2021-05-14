# my_set = {1,2,3,4,5}

# print(my_set)

#convert a list into a set. return items only once. 
my_list = [1,2,3,4,5,5]
new_set = set(my_list)
print('The set is: ', new_set)

## SETS METHODS
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set))
print(my_set.discard(5))
##**
print(my_set.difference_update(your_set))


print(my_set.union(your_set))

#true or false.
print(your_set.issuperset(my_set))
