import sys
from operator import truediv, mul, add, sub

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}


def calculate(s):
    if s.isdigit():
        return float(s)
    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))
    else:
        print('invalid calculation')
        print(exit(0))


calc = input("Input Calculation:\n")
print('Finish')
print("Answer: " + str(calculate(calc)))
