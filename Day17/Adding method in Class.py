

class user:


    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Adding method in Class
    def follow (self ,user):
        user.followers += 1
        self.following += 1


user_1 = user("0112", "Vivek")
user_2 = user("5454", "Kevik")
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_1.followers)
print(user_2.following)
