#using list() function - range() directly into a list using the list()
countin_no = list(range(6))
print(countin_no)
# look what am planing
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# squares of 10 natural number
squares=[]
for number in range(1,11):
	square = (number ** 2)
	squares.append(square)
	#squares.append(number ** 2)
print(squares)
#max()function
print(f"The max squares: {max(squares)}")
#min()function
print(f"The min squares: {min(squares)}")
#sum()function
print(f"The sum squares: {sum(squares)}")
#list comprehensions
square = [(value ** 2) for value in range(1,11)];
print(square)
#slicing
print(square[0:8])
print(square[2:8])
print(square[:8])
print(square[5:])
print(square[-3:])
#You can include a third value in the brackets indicating a slice. If a third value is included, this tells Python how many items to skip between items in the specified range.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
#Looping Through a Slice
for player in players[:3]:
	print(player.title())