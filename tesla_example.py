
age = ''
def driverAge():
    age = int(input('What is your age? '))
    if  (age >18):
        print('Powering on!')
        
    if (age == 18):
        print('COngrats on your first year of driving!')
    elif (age < 18):
        print('Sorry, you are too young. Powering Off!')
driverAge()