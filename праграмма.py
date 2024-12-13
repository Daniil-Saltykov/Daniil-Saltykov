a = int(input("введи первое число: "))
b = int(input("введи второе число: "))
sign = input("Введи знак:")


def sub(num1, num2):
    return a - b

def add(num1, num2):
    return a + b


def divide(num1, num2):
    if b != 0:
        return a // b

    def mult(num1, num2):
        return a * b


if sign == "-":
    print(sub(a, b))

if sign == "+":
    print(add(a, b))

if sign == "//":
    print(divide(a, b))

if sign == "*":
    print(mult(a, b))
    calculator()