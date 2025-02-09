class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

        print("New user being created...")


    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Edu")
user2 = User("002",  "and")

user1.follow(user2)

print(user1.followers)
print(user2.followers)

user2.follow(user1)

print(user1.followers)
print(user2.followers)

