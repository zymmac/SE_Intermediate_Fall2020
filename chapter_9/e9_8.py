#Admin
from e9_3 import User

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


admin = Admin('alexandre', 'Costa', 'zymmac', '1234')
admin.privileges.show_privileges()