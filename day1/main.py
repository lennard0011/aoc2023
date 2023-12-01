import os
print (os.getcwd())

def getFirstDigit(myString):
    for i in myString:
        if i.isdigit():
            return int(i)
        
def matchWrittenNumber(myString):
    if myString.startswith('one'):
        return 1
    if myString.startswith('two'):
        return 2
    if myString.startswith('three'):
        return 3
    if myString.startswith('four'):
        return 4
    if myString.startswith('five'):
        return 5
    if myString.startswith('six'):
        return 6
    if myString.startswith('seven'):
        return 7
    if myString.startswith('eight'):
        return 8
    if myString.startswith('nine'):
        return 9
    if myString.startswith('ten'):
        return 10
    return None
        

def getFirstDigitOrWrittenNumber(myString):
    for index, char in enumerate(myString):
        if char.isdigit():
            return int(char)
        matchedWordNumber = matchWrittenNumber(myString[index:])
        if matchedWordNumber != None:
            return matchedWordNumber
    return None
        
   
def invertString(myString):
    return myString[::-1]

def getLastDigit(myString, searchFunction):
    lastDigit = None
    for index, _ in enumerate(myString):
        currentDigit = searchFunction(myString[index:])
        if currentDigit != None:
            lastDigit = currentDigit
    return lastDigit

def run(part=1, file='test'):
    textFile = open(f"./day1/{file}{part}.txt")
    lines = textFile.readlines()

    numbers = []
    sum = 0

    searchFunction = getFirstDigit if part == 1 else getFirstDigitOrWrittenNumber

    for row in lines:
        firstNumber = searchFunction(row)
        secondNumber = getLastDigit(row, searchFunction)
        total = firstNumber * 10 + secondNumber
        numbers.append(total)
        sum += total

    print('numbers: ', numbers)
    print('sum: ', sum)

run(2, 'input')