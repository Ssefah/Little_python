"""The remove() method deletes only the first occurrence of the value you specify.
If there’s a possibility the value appears more than once in the list, you’ll
need to use a loop to make sure all occurrences of the value are removed."""
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
#motorcycles.remove('ducati')
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")
print(motorcycles)