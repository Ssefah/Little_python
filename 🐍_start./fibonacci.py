number = int(input("Enter number:"))


def fibonacci(number):
    if (number == 1 or number == 0):
        return (number)
    else:
        return (fibonacci(number-1) + fibonacci(number-2))


answer = (fibonacci(number))
print(f"The fibonacci of is {number}: {answer}.")
