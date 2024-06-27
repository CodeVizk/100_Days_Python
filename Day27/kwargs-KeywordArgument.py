 # We can us unlimited keyword arguments using **kwargs

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


def multiply(*args):
    result = 0
    for n in args:
        result *= args
    return result


# Using **kwargs
def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    # kwargs store in a dictionary, so we can use all the methods of dictionary
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(3, add=4, multiply=23)
