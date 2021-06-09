# translate the txt file into Japanese.
import Translator
try:
    with open('/Users/arnenyeck/Desktop/Repositories/complete_python_developer/OOP/translatorTest.txt', mode='r') as my_file:
        text = my_file.read()
        translation = Translator.translate(text)
        print(translation)
except FileNotFoundError as e:
    print('Check your file path!')
