char = input("please enter a string")
def withoutVowles(text):
    vowels = ['a','e','i','o','u']
    text = text.lower()
    result = ""
    for char in text:
        if char.lower() in vowels:
            result += ""
            result += char
    print(result)
    