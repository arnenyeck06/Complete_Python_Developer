
#dict -- key,valeu pair

# dictionary = [
#     {
#     'a':[1,2,3],
#     'b':'hello',
#     'x':True
# }

my_list = [
    {
    'a':[4,5,6],
    'b':'hello',
    'x':True 
    },
    {
    'a':[4,5,8],
    'b':'I am testing',
    'x':True
}
]
print(my_list[0]['a'][2])

# print(dictionary['a'][1])

dictionary = {
    123:[1,2,3],
    'greeting':'hello',
    'is_Magic':True
}
print(dictionary[123])

# checking keys and values
print('123' in dictionary.keys())
print('hello'in dictionary.values())

user = {
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}
print(user.popitem())
print(user.clear())
print(user.update({'age':29}))