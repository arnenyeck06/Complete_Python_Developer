def sum(num1, num2):
    return num1 + num2 ## without 'return' the output will be NONE.
total = sum(10,5)
print(sum(10,total))


def sum2(num3, num4):
    def another_func(num3, num4):
        return num3 + num4
    return another_func(num3, num4)

total2 = sum(10, 20)
print(total2)