#Creating a class
class user:


# Adding attribute in a class
    # initialising / constructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0

user_1 = user ("0910", "Vivek")
print(user_1.id)
# Sometimes we don't want to always add a parameters, so we just add an attribute
# with a default value and not specifying in the __init__ like self.follower = 0





