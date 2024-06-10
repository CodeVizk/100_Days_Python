# Higher order function takes another function as a input
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def calculator(n1, n2, func):
    return func(n1, n2)


# Calling calculator
result = calculator(4, 3, add)
print(result)

result2 = calculator(5, 2, subtract)
print(result2)
