"""Celsius=(5/9)*(Fahrenheit-32);
Fahrenheit=(((9/5)*Celsius)+32);"""
for Celsius in range(0, 301, 20):
    {

        print(f"{Celsius:>3}°C {(((9/5)*Celsius)+32):>4}°F")
    }
for Fahrenheit in range(0, 301, 20):
    {

        print(f"{Fahrenheit:>3}°F {round(((5/9)*(Fahrenheit-32)),3):>6}°C")
    }
