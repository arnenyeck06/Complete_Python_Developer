
amazon_cart = ['notebooks', 
'sunglasses',
'toys',
'grapes']
# list slicing
print(amazon_cart[0::2])

#list are immutable
#replace notebook by a laptop. 
amazon_cart[0] = 'laptop'
new_cart = amazon_cart
print(new_cart)

print(amazon_cart)


#MATRIX
matrix = [
[1,2,3],
[2,4,6],
[7,8,9]
]
print(matrix[0][1])

# basket = [1,2,3,4,5]
# # add something in the list
# #add 
# basket.append(100)
# new_list = basket
# print(basket)

# basket.insert(5, 200) # add 200 at the 5th position
# new_basket = basket
# print(basket)

# # # removing
# # basket.pop()
# # basket.pop()
# # print(basket)

# basket.remove(100)
# print(basket) 

# basket.clear()
# print(new_basket)


basket = ['a', 'b', 'c', 'd','e']
print(basket.index('d', 0, 4)) # look for d starting at index 0, stops at 4

# is d in basket?
print('d' in basket)
print(basket.count('d')) # number of d in the list
print(basket[::-1]) # reverse

#(Start; stop)
print(list(range(1,100)))

# Joining
new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'slim', 'shady'])
print(new_sentence)


#List unpacking
# a,b,c = [1,2,3]
print(a)
print(b)

a,b,c, * other, d = [1,2,3,4,5,6,7,8,9]

