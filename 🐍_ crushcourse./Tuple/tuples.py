#Tuples can't not be modification
#Use them when you want to store a set of values that should not be changed throughout the life of a program.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250 generates an error
print()
#Looping Through All Values in a Tuple
#Writing over a Tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
	