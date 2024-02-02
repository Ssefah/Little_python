def make_pizza(*toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print()
print()
#Using Arbitrary Keyword Arguments **user_info cause Python to create an empty dictionary called user_info and pack whatever name- value pairs it receives into this dictiona
def build_profile(first, last, **user_info):#**kwargs
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info
user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)