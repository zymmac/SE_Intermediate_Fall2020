import unittest
from e11_3 import Employee

class TestEmployee(unittest.TestCase):
    """ Test class employee"""

    def setUp(self):
        """Create an instance of employee to use in all tests"""
        self.employee = Employee("Alexandre", "Costa", 50000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary,55000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary,60000)

    

if __name__ == "__main__":
    unittest.main()