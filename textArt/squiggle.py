def squiggle(string, rows):
    squiggleOfString = ""

    for i in range(rows):
        for x in range(len(string) + 1):
            squiggleOfString += x * " " + string + "\n"
        for x in range(len(string) + 1):
            squiggleOfString += (len(string) - x) * " " + string + "\n"

    return squiggleOfString

givenString = input("What is your string: ")
rows = int(input("What is the amount of rows: "))
print(squiggle(givenString, rows))