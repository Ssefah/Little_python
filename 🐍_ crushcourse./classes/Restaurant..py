class Restaurant:
	"""Restaurant class"""
	#print()
	
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		"""Describes the restaurant"""
		print(f"{self.restaurant_name} is a Italian traditional restaurnt")
		print(f"Different cuisines are prepared at {self.restaurant_name}")
	def open_restaurant(self):
		print(f"{self.restaurant_name} is open between 08:00 - 23:00")
my_restaurant = Restaurant('Itabase','Pizza')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()