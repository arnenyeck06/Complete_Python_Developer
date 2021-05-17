# is_old = True
# is_licenced = True

# if is_old:
#     print("You are old enough to drive")
# print('check mate!')

is_old = True
is_licenced = True  
if is_old:
    print('check')
elif is_licenced:
    print('check')
print('Good to go!')

# to check both condition to be true.
if is_old and is_licenced:
    print('Good to go!you are old enough and you have a licence')
else:
    print('Next!')


    ## TERNARY OPERATOR
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"


