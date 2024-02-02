"""Celsius=(5/9)*(Fahrenheit-32);
Fahrenheit=(((9/5)*Celsius)+32);"""
while (1):
    print("\tConvert:")
    print("1.Celsius to Fahrenheit")
    print("2.Fahrenheit to Celsius.")
    option = int(input("Enter preference:"))

    def to_Fahrenheit(Celsius):
        Fahrenheit = round((((9/5)*Celsius)+32), 3)
        return Fahrenheit

    def to_Celsius(Fahrenheit):
        Celsius = round(((5/9)*(Fahrenheit-32)), 3)
        return Celsius
    if (option == 1):
        Celsius = float(input("Enter Celsius value:"))
        {print(f"  {to_Fahrenheit(Celsius)}°F")
         }
    elif (option == 2):
        Fahrenheit = float(input("Enter Fahrenheit value:"))
        {print(f"  {to_Celsius(Fahrenheit)}°C")
         }
    else:
        {
            print("\tInvalid Input.")}
