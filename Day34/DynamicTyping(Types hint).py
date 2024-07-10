# to avoid confusion when declaring any variable we use Type hint

number: int
is_right: bool
decimal: float
name: str

# age = "ten"
# will give Error line as wrong data type is entered


def add(age: int):
    return age + 10


add(12)

# Type hint tells what will should be returned or expected


def age_check(num: int) -> bool:
    if num > 18:
        age_is_right = True
    else:
        age_is_right = False

    return age_is_right
