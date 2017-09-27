def add_two_numbers(number1, number2):
    answer = 0
    answer = number1 + number2
    return answer

add_two_numbers(1, 5)

def multiplyNumbers(firstNumber, secondNumber):
    result = 0
    for index in range (secondNumber):
        result = add_two_numbers(firstNumber, result)

    #print result

multiplyNumbers(4,5)

def myPower(firstNumber, secondNumber):

    if secondNumber == 0 :
        return 1
    else:
        answer = myPower(firstNumber, secondNumber -1)
        
        return firstNumber * answer

print myPower(3,2)
