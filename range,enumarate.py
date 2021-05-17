for numbers in range(0,10):
    print(numbers)

#Instead of output showing as a column, convert the range to a list

for x in range(1):
    print(list(range(0, 10)))


## ENUMARATE
for i,char in enumerate('Helloooo'):
    print(i, char)

# Expl: print the value 50 
for i, char in enumerate(list(range(100))):
    if char == 50:
        print('The index of 50 is: ', char)