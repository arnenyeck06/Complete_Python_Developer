# name = input('What is your name?')
# print('Hello ' + name) # we stored the input into name.

long_string = '''
WOW
O O
___

'''
print(long_string)  

first_name = 'Elie'
last_name = 'Nyeck' 
full_name = first_name + ' ' + last_name
print(full_name)    

# String Concatenation
print('Hello' + ' ' + 'Elie ')

# Converting 100 to str, to int, check type
print(type(int(str(100)))) 

a = str(100)
b = int(a)
c = type(b)
print(c) # same as previous.

##Escape Sequence
# Use \ where there is apostrophes. \t indents
weather = "It\\s \"kind of\" sunny"
print(weather)

##******####### Formatter strings with f
name = 'Johnny'
age = 55

##print('hi' + name +'You are' +str(age) + 'years old')
print(f'hi {name}. You are {age} years  old')

#Using the dot format
print('hi{}. You are{} years old'.format(name, age))     

####******Indexes, String slicing
selfish = 'me me me'
        #  01234567 indexes
print(selfish[3])

# [start:stop]
print(selfish[0:5])
#[start"stop:stepover] stepover by..
print(selfish[2:3:3])
print(selfish[::-1]) # reverse

quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize()) 
print(quote.lower()) 
print(quote.find('be')) ## find the occurence
print(quote.replace('be', 'QUIT'))

## BOOLEANS
name = 'Arne'
is_cool = False

is_cool = True

print(bool(1))

## TYPE CONVERSIONS

name = 'Arne Nyeck'
age = 50
relationship_status = 'single'
#change relation status, hard code
relationship_status = 'It\'s complicated'
print(relationship_status)

#EXample

#birth_year = input('What year were you born?')
#age = 2021 - birth_year
#print(f'Your age is: {age}')
## get an error, so convert birth year into int
birth_year = input('What year were you born?')
age = 2021 - int(birth_year)
print(f'Your age is: {age}')

