class User():
    def sign_in(self):
        print('logged in')


class wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print('f{self.arrows} remaining')

    def run(self):
        print('ran really fast')

# a hybrid user that have all the attributes: name, power, arrows


class HybridBorg(wizard, archer):
    def __initi__(self, name, power, arrows):
        archer.__init__(self, name, arrows)
        wizard.__init__(self, name, power)


hb1 = HybridBorg('Arne', 50, 100)
print(hb1.sign_in())
print(hb1.check_arrows())
