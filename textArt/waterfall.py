def waterFall(string):
    waterFallString = ""

    for i in range(1, len(string) + 1):
        waterFallString += string[0:i] + "\n"

    return waterFallString

givenString = input("What is your string: ")
print(waterFall(givenString))