""" Classes: User, Admin, Privileges """

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

class Admin(User):
    """
    A special kind of user
    """
    def __init__(self, first_name, last_name, nickname, password):
        super().__init__(first_name, last_name, nickname, password)
        self.privileges = Privileges(['can add post','can delete post', 'can ban user'])

class Privileges():
    """
    privileges of a user
    """

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print(f'This User has the following privileges: \n')
        for p in self.privileges:
            print(f'\t- {p}')


def main():
    admin = Admin('alexandre', 'Costa', 'zymmac', '1234')
    admin.privileges.show_privileges()

if __name__ == '__main__':
    main()