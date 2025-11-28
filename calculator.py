import random
# todo 1 import random
# todo 2 define add, subtract, multiply, divide functions
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "undefine"
    return a/b
# todo 3 handle division by zero in divide
# todo 4 create calculator dictionary for operators
calculate = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
# todo 5 get first number, operator, second number from user
first_num = float(input("Enter first number: "))
operator = input("Enter operator:+, _, *, / ")
second_num = float(input("Enter second number: "))
# todo 6 validate operator and compute initial result
if operator in calculate:
    result = calculate[operator](first_num, second_num)
    print(f"Result: {result}")
# todo 7 start loop to continue calculations
while True:
    choice = input("Do you want to continue? (y/n): ")
    if choice != "y":
        print("Thank you for using the calculator")
        break
    if operator in calculate:
        operator = input("Enter operator:+, _, *, /  ")
        next_num = float(input("Enter next number: "))
        result = calculate[operator](result, next_num)
        print(f"Result: {result}")
# todo 8 ask user to continue or exit
# todo 9 get next operator and number
# todo 10 compute and print updated result
    else:
        print("invalid operation")
        exit()

# todo 11 handle invalid operator
