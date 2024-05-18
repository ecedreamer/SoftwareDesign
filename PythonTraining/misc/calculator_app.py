# making a calculator app for addition, subtraction, multiplication & division
# \n is a new line character or line break

def do_addition(x, y):
    addition = x + y
    print(addition)

def do_subtraction(x, y):
    subtraction = x - y
    print(subtraction)

def do_multiplication(u, v):
    product = u * v
    print(product)

def get_division(num, denom):
    if denom == 0:
        print("Can not be devided by zero")
        exit()
    div = num / denom
    print(div)


operator = input("Enter + for addition\nEnter - for subtraction\nEnter * for product\nEnter / for division\n")

if operator not in ["+", "-", "*", "/"]:
    print("You have entered an invalid operator")
    exit()

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

if operator == "+":
    do_addition(first_number, second_number)
elif operator == "-":
    do_subtraction(first_number, second_number)
elif operator == "*":
    do_multiplication(first_number, second_number)
elif operator == "/":
    get_division(first_number, second_number)