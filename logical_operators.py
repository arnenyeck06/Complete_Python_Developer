is_magician = False
is_expert = True
# check if magician AND expert: " you are a master magician"

if is_magician and is_expert:
    print('You are a master magician')

# if magician but not expert

if is_magician and not is_expert:
    print('At least, you are getting there.')

# if you're not a magician
elif not is_magician:
    print('You need magic powers')



