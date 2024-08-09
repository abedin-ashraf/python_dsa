stringArray = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def convertToString(num):
    if num == 0:
        return
    lastdigit = stringArray[num % 10]
    convertToString(num // 10)
    print(lastdigit)


convertToString(1920)

