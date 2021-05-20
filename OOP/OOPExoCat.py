

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
Milo = Cat('Milo', 5)
Duke = Cat('Duke', 4)
Prince = Cat('Prince', 1)


# 2 Create a function that finds the oldest cat, then print the oldest cat
def OldestCat(*args):
    return max(args)


print(
    f'the oldest cat is {OldestCat(Milo.age, Duke.age, Prince.age)} years old')
