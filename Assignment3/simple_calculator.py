"""
File: simple_calculator.py
ID:0711506
Author:王偉誠
Cite:翁子婷
----------------------------
This program reads strings as expressions
and computes the answer of the user's input.
There will be 2 operations: addition and subtraction
If the input is not in correct format, "Illegal format"
will be printed on console.
"""



def check_plus(str1):
    """
    To check error for the addition part.
    """
    number1 = ""
    number2 = ""
    b = False
    plus = False
    for i in str1:
        if i == "+":
            plus = True
            continue
        if not plus:
            number1 += i
        else:
            number2 += i
    for i in number1:
        if i == ".":
            continue
        else:
            if i.isalpha():
                b = True
                break
    for i in number2:
        if i == ".":
            continue
        else:
            if i.isalpha():
                b = True
                break
    return b


def check_minus(str2):
    """
    To check error for the subtraction part.
    """
    number1 = ""
    number2 = ""
    b = False
    minus = False
    for i in str2:
        if i == "-":
            minus = True
            continue
        if not minus:
            number1 += i
        else:
            number2 += i
    for i in number1:
        if i == ".":
            continue
        else:
            if i.isalpha():
                b = True
                break
    for i in number2:
        if i == ".":
            continue
        else:
            if i.isalpha():
                b = True
                break
    return b


def addition(str1):
    """
    This method is for situation which the first_input is 1.
    For example, if you input 2+1, this method will calculate and return 3.0.
    """
    while True:
        while "+" not in str1 or " " in str1:
            print("Illegal format")
            str1 = input("Give me a corresponding expression of 2 numbers: ")
        if check_plus(str1):
            print("Illegal format")
            str1 = input("Give me a corresponding expression of 2 numbers: ")
        else:
            break
    number1 = ""
    number2 = ""
    plus = False
    for i in str1:
        if i == "+":
            plus = True
            continue
        if not plus:
            number1 += i
        else:
            number2 += i
    answer = float(number1) + float(number2)
    return answer


def subtraction(str2):
    """
    This method is for situation which the first_input is 2.
    For example, if you input 2-1, this method will calculate and return 1.0.
    """
    while True:
        while "-" not in str2 or " " in str2:
            print("Illegal format")
            str2 = input("Give me a corresponding expression of 2 numbers: ")
        if check_minus(str2):
            print("Illegal format")
            str2 = input("Give me a corresponding expression of 2 numbers: ")
        else:
            break
    number1 = ""
    number2 = ""
    plus = False
    for i in str2:
        if i == "-":
            plus = True
            continue
        if not plus:
            number1 += i
        else:
            number2 += i
    answer = float(number1) - float(number2)
    return answer


def main():
    """
    This program can calculate (only addition and subtraction) the number you input.
    For example, if you input 1-1, it will print 0.0.
    """
    while True:
        n = input("(addition=1, subtraction=2, or 0 to exit): ")
        if n == '1':
            str1 = input("Give me a corresponding expression of 2 numbers: ")
            ans = addition(str1)
            print("The answer is: " + str(ans))
        elif n == '2':
            str2 = input("Give me a corresponding expression of 2 numbers: ")
            ans = subtraction(str2)
            print("The answer is: "+str(ans))
        elif n == '0':
            break
        else:
            print("Illegal format")
            continue


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
