#Admin
from e9_3 import User

class Admin(User):
    """
    A special kind of user
    """
    def __init__(self, first_name, last_name, nickname, password):
        super().__init__(first_name, last_name, nickname, password)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f'Username: {self.first_name.title()} {self.last_name.title()}\n')
        for p in self.privileges:
            print(f'\t- {p}')

admin = Admin('alexandre', 'Costa', 'zymmac', '1234')
admin.show_privileges()

