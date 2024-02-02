requested_toppings = ['mushrooms', 'onions', 'pineapple']
answer = 'mushrooms' in requested_toppings
print(answer)
answer = 'pepperoni' in requested_toppings
print(answer)
#Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")
	
#Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
print("\nFinished making your pizza!")
#amusement park
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25.")
else:
	print("Your admission cost is $40.")