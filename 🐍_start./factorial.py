"""number=int(input("Enter number:"));
def mystery(number):
	if(number < 2):
		return 1;
	else:
		return (number* (mystery(number - 1)));
answer=(mystery(number));
print(f"The factorial is of {number}: {answer}.")"""
num = int(input("Enter number:"))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print(fact)
