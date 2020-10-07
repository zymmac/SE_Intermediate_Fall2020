# Number Served

class Restaurant():
    """
    Store a restaurant name and a cuisine type and describes itseld
    """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} - cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f'We\'re now open!')

    def increment_number_served(self, total):
        self.number_served += total
        return self.number_served

restaurant = Restaurant("La Chaumière", 'french')
print(restaurant.number_served)
restaurant.number_served = 1
print(restaurant.number_served)
print(restaurant.increment_number_served(10))