""" Class User with first and last name """

class User():
    """
    A user has a first_name and last_name as attr.
    """
    def __init__(self, first_name, last_name, nickname, password):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.password = password

    def describe_user(self):
        full_name = f'{self.first_name} {self.last_name}'.title()
        print("User:", full_name)
        print("Nickname:", self.nickname)
        print("Password:", self.password)

    def greet_user(self):
        full_name = f'{self.first_name} {self.last_name}'.title()
        print(f'Welcome, {full_name.title()}!')

def main():
    user1 = User("alexandre", 'mendes', 'zymmac', '1234')
    user2 = User('patricia','silva', 'pbarbosa', '5678')
    user3 = User('isabela','costa','pinx','9876')

    userlist = [user1,user2,user3]

    for user in userlist:
        user.describe_user()
        user.greet_user()
        print('')

if __name__ == '__main__':
    main()


