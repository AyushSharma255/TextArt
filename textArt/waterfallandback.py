def waterFallAndBack(string):
    waterFallString = ""

    for i in range(1, len(string) + 1):
        waterFallString += string[0:i] + "\n"
    for i in range(len(string) + 1, 0, -1):
        waterFallString += string[0:i] + "\n"

    return waterFallString

givenString = input("What is your string: ")
print(waterFallAndBack(givenString))