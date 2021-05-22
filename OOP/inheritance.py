class User:
    def sign_in(self):
        print('logged in')

# create subclasses. wizrd, archr...are users. to access the log in,
# pass in the (user)


class wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class archer():
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left-{self.num_arrows}')


wizard1 = wizard('Merlin', 50)
archer1 = archer('Robin', 100)
wizard1.attack()
archer1.attack()


wizard1 = wizard('Merlin', 50)
print(isinstance(wizard1, wizard))
