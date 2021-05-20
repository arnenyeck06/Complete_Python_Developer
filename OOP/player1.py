class PlayerCharacter:
    # class object attribute membership
    membership = True

    def __init__(self, name, age):
        self.name = name  # 'Self' refers to the class.
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Arne', 29)
player2 = PlayerCharacter('Danna', 22)

print(player1)
print(player2)
print(player2.membership)
