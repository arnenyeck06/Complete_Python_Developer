# method on the actual class, no need to instantiate
class PlayerCharacter:
    # class object attribute membership
    membership = True

    def __init__(self, name, age):
        self.name = name  # 'Self' refers to the class.
        self.age = age

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1, num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player3 = PlayerCharacter.adding_things(2, 3)


# REVOIR LES ERREURS
