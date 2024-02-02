class User:
	""""""
	
	def 	__init__(self,first_name,last_name,):
		self.first_name = first_name
		self.last_name = last_name
		
		
	def describe_user(self):
		"""prints a summary of the user’s information."""
		print(f"Username: {self.first_name} {self.last_name}")
		
		
	def greet_user(self):
		"""personalized greeting to the user"""
		print(f"Hello {self.first_name} {self.last_name} ")

user_1 = User('Farouq','Ssemmambo')
print(f"Name:{user_1.first_name} {user_1.last_name}")
user_1.describe_user()
user_1.greet_user()
