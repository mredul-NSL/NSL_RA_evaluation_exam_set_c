def do_math(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        return "You can't divide by zero"


# lets call the method with x, y where x and y are two numbers
print(do_math(10, 0))
print(do_math(10, 2))