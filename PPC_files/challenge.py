users = []
user_bob = {"name": "bob", "title": "bobster"}
user_max = {"name": "ma", "title": "mxout"}

users.append(user_bob)
users.append(user_max)

class User():
    def __init__(self, data):
        for key in data:
            setattr(self, key, data[key])

for user in users:
    user = User(user)
    print(user.name, user.title)

    
users = []
user_bob = {"name": "bob", "title": "bobster"}
user_max = {"name": "ma", "title": "mxout"}
users.append(user_bob)
users.append(user_max)

class User():
    def __init__(self, data):
        for key in data:
            setattr(self, key, data[key])

maxx = User(user_max)
print(maxx.name)
print(maxx.title)