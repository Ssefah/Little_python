﻿motorcycles = ['honda', 'yamaha', 'suzuki','ducati', 'bmw']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print()
print(popped_motorcycle)
print()
print(motorcycles)
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
print(motorcycles)
print()
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)
print()