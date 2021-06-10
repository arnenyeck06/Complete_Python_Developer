# using https://regexone.com/ , with its code generator.


# password at least 8 char long
# any letter, numbers, $%#@
# has to end with a number

import re

password = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
string = 'vvxvxhbchsxcjsecret3'

checkPassword = password.search(string)
print(checkPassword)
