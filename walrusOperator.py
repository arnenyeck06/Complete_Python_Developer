a = 'hellooooooooooooooo'

if(len(a) > 10):
    print(f'too long, {len(a)} elements')

# walrus operator wants you to assign len(a) to n.
# it cleans up your code too.

a = 'hellooooooooooooooo'

if((n := len(a)) > 10):
    print(f'too long, {n} elements')
