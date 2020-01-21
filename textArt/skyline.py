def skyline(string):
    newString = ""
    capital = False

    for i in range(len(string)):
        if not capital:
            newString += string[i].lower()
        elif capital:
            newString += string[i].upper()

        capital = not capital

    return newString

givenString = input("What is your string: ")
print(skyline(givenString))