﻿def favorite_book(title):
	'''Display a favorite book title.'''

	print(f"One of my favorite books is , {title.title()}!")
favorite_book("Alice in the wondaland.\n")
#pets
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
#Keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
#Default Values
def describe_pet(pet_name, animal_type='dog'):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')