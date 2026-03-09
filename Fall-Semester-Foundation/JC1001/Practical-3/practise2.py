letter = input("please enter a letter")
a = len(letter)
letter = letter.lower()
if a != 1:
    print("Invaild input")
else  :
    if letter == ['a','e','i','o','u']:
        print(f'{letter} is a vowel')
    elif letter == ['y'] :
        print("A y can sometimes be a vowel and sometimes is not ")
    else :
        print(f'A {letter} is a consonant')