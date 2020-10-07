#Restaurant

class Restaurant():
    """
    Store a restaurant name and a cuisine type and describes itseld
    """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} - cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f'We\'re now open!')
    
if __name__ == '__main__':
    restaurant = Restaurant('Yuzu-an', 'japanese')
    print(restaurant.restaurant_name)
    print(restaurant.cuisine_type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    