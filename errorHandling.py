#  age = int(input('what is your age? '))
# print(age)

# for the error to be handled, convert to int, wrap in a loop.


while True:
    try:
        age = int(input('what is your age? '))
        print(age)
    except:
        print('Please, enter a number')
    else:
        print('Thank you')
        break


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(err)


print(sum(2, 3))
