bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
for bicycle in bicycles:
	print(f"I would like to purchase a {bicycle}");
"""
for i in range(4):
	print(bicycles[i])"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#modifying 
motorcycles[0] = 'ducati'
print(motorcycles)
#appending or adding to a list
motorcycles.append('honda')
print(motorcycles)
#inserting insert(position,element)
motorcycles.insert(0,"bmw")
print(motorcycles)
#deleting elements del motorcycles[index]
del motorcycles[0]
print(motorcycles)
friends=["sameul",35.96,"fred","ssefah","haz","littlechico"];
for friend in friends:
	print(f"My friend is {friend}");