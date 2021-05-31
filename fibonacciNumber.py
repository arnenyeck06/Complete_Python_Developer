def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        tempVar = a
        a = b
        b = tempVar + b


for x in fib(21):
    print(x)


# let's do the same with a list

def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        tempVar = a
        a = b
        b = tempVar + b
    return result


print(fib2(10))
