alien_0 = {'color': 'green', 'points'
:5}
#Accessing Values in a Dictionary
print(alien_0['color'])
print(alien_0['points'])
#Adding New Key-Value Pairs
alien_0['x_position'] = 0;
alien_0['y_position'] = 25;
#Modifying Values in a Dictionary
alien_0['color'] = 'yellow'
#Using get() to Access Values- Error Handling
point_value = alien_0.get('me','No point value assigned.')
print(point_value)
print(alien_0)
print()
#Removing Key-Value Pairs
del alien_0['points']
print(alien_0)
#A Dictionary of Similar Objects
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")