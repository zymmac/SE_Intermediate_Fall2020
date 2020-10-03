from unittest import TestCase, main
from city_functions import location

class TestLocation(TestCase):
    """Test the function location"""

    def test_city_country(self):
        my_city_country = location("santiago", "chile")
        self.assertEqual(my_city_country, "Santiago, Chile")

    def test_city_country_population(self):
        my_city_country = location("santiago", "chile", 5000000)
        self.assertEqual(my_city_country, "Santiago, Chile - population 5000000")

if __name__ == '__main__':
    main()

