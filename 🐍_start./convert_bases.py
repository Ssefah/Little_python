print("**********Convert.**********")
print("1.Binary.")
print("2.Octal.")
print("3.Hex Decimal.")
print("4.Exit.")
option = int(input("Enter preference:"))


def binary():
    print("1.Binary to decimal.")
    print("2.Decimal to binary.")
    options = int(input("Enter preference:"))
    if options == 2:
        number = int(input("Enter decimal number:"))
        print(f"Binary: {(number):b}")
    elif options == 1:
        number = (input("Enter binary number:"))
        print(f"Decimal: {int(number,2)}")
    else:
        print(("Invalid Input."))


def octal():
    print("1.Octal to decimal.")
    print("2.Decimal to octal.")
    options1 = int(input("Enter preference:"))
    if options1 == 2:
        number = int(input("Enter decimal number:"))
        print(f"Octal: {(number):o}")
    elif options1 == 1:
        number = (input("Enter octal number:"))
        print(f"Decimal: {int(number,8)}")
    else:
        print(("Invalid Input."))


def hex_decimal():
    print("1.Hex to decimal.")
    print("2.Decimal to hex.")
    options2 = int(input("Enter preference:"))
    if options2 == 2:
        number = int(input("Enter decimal number:"))
        print(f"Hex_Decimal: {(number):x}")
    elif options2 == 1:
        number = (input("Enter Hex decimal number:"))
        print(f"Demical: {int(number,16)}")
    else:
        print(("Invalid Input."))


if option == 1:
    binary()
elif option == 2:
    octal()
elif option == 3:
    hex_decimal()
elif option == 4:
    pass
else:
    print(("Invalid Input."))
