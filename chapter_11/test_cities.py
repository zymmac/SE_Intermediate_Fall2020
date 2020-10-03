from unittest import TestCase, main
from city_functions import location

class TestLocation(TestCase):
    """Test the function location"""

    def test_city_country(self):
        my_city_country = location("santiago", "chile")
        self.assertEqual(my_city_country, "Santiago, Chile")

if __name__ == '__main__':
    main()

