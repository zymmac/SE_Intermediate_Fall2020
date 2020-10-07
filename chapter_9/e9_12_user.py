""" Class: User """

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
