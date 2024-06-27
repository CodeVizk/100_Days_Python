# Developers use *args/*xyz to specify many arguments can be taken for a function
# These are unlimited positional arguments


def printer(*args):
    for n in args:
        print(n)


a = "A"
printer(1, 23, 4, 5, "Yo", a)
