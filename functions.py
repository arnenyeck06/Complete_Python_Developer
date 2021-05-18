# how to define functions.

def say_hello():
    print('hello')
say_hello()


# If I want to show the Xmas tree multiple times.

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
def tree():
    for x in picture:
        for y in x:
            if (y == 1):
                print('*', end='')
            else:
                print(' ', end="")
        print(' ')
tree()

tree()
