#simple calculator
def add(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    
    if y == 0:
        return "Erro! division by Zero"
    else:
        return x / y
    
num1 = float(input("enter first number"))
num2 = float(input("enter the second number"))
operator = input("enter the operator (+, -,*,/):")

if operator == "+":
    print("result" , add(num1, num2))

if operator == "-":
    print("result" , subtraction(num1, num2))

if operator == "*":
    print("result" , multiplication(num1, num2))

if operator == "/":
    print("result" , division(num1, num2))

