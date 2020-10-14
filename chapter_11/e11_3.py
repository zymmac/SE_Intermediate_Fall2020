"""Class Employee """
class Employee(object):
    """
    employee has a first name, last name and annual salary.
    methods: give_raise()
    """
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise=5000):
        """Increases annual salary by specified ammount. 5000 is default"""
        self.annual_salary += salary_raise

    
