# Examples
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(4, 45, 2))


# making my own kwargs

class Car:
    def __init__(self, **kwargs):
        # we use .get() so if there are no parameter for it, it returns none rather than an error
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.specs = kwargs.get("specs")
        # This is  also correct but it will return error when not specified
        self.tyre_size = kwargs["tyre_size"]


my_car = Car(make="Bugatti", model="Tourbillion", colour="Blue")
print(my_car.make,
      my_car.model,
      my_car.specs,
      # This will return error rather than none so we use .get()
      # my_car.tyre_size
      )
