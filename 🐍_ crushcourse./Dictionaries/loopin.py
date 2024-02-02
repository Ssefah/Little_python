user_0 = {
'username': 'Ssefah',
'first_name': 'Farouq',
'last_name': 'Ssemmambo',
}
#The method items(), which returns a list of key-value pairs. 
for Key, Value in user_0.items():
	print(f"Key: {Key}")
	print(f"Value: {Value}\n")
#
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")
print()
print()
#Looping Through All the Keys in a Dictionary
#The method keys(), which returns a list of key
for name in favorite_languages.keys():
	print(name.title())
print()
print()
#The method values(), which returns a list of values without any keys
for language in favorite_languages.values():
	print(language.title())
print()
print()
#The function set(), which returns a list of values without any keys and repetition, each item mustbe unique:
for language in set(favorite_languages.values()):
	print(language.title())
print()
print()
#lists
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(f"Hi {name.title()}.")
	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")
#using not
print()
print()
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!"
)
print()
print()
#Looping Through a Dictionary’s Keys in a Particular Order [SORTING]
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")