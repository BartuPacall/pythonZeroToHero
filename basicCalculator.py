# Basic Calculator Python

op = input("Choose an operand (+ - * /) :")


while True:
    try : 
        x = input("Enter first number :")
        number1 = int(x)
        break
    except  ValueError:
        print("Element not founded")

while True:
    try : 
        y= input("Enter second number :")
        number2= int(y)
        break
    except  ValueError:
        print("Element not founded")

if op == "+":
    print(number1 + number2)
elif op == "-":
    print(number1 - number2)
elif op == "/":
    if number2 != 0:
        print(number1 / number2)
    else:
        print("Error: Division by zero is not allowed.")
elif op == "*":
    print(number1 * number2)
else:
    print("Operation not recognized. Please choose a valid operand : +, -, *, /")