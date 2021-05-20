# new python variable called: Non local


# Scope- What variables do i have access to

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)


outer()

x = 5
print(x)
