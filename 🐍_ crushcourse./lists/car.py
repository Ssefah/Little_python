cars = ['bmw', 'audi', 'toyota', 'subaru']
#alphabetical .sort() methods
cars.sort()
print(cars)
#reverse alphabetical
cars.sort(reverse = True)
print(cars)
print()
#sorted() function, Sorting a List Temporarily
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
# sorted() accepts reverse=True arguments

# using reverse() function reverses the order of the list:
print()
cars.reverse()
print(cars)
# len() 
print(f"The length is {len(cars)}.")