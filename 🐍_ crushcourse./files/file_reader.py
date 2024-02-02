filename = 'pi_digits.dat'
try:
	with open(filename) as file_object:
	 contents = file_object.read()
	print(contents) 
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")