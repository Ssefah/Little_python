import sys
Balance=15000.00;
def exit():
		print("-----------Take your receipt!!!-----------");
		print("-----Thank you for using Atm Banking");
def check_bal():
		global Balance;
		Balance= Balance
		print(f"\tCurrent Balance: {round(Balance,3)}shs");
def withdraw():
		global Balance;
		print(f"\tCurrent Balance: {round(Balance,3)}shs");
		withdraw_amount=float(input("Enter withdraw amount:"))
		if (withdraw_amount >= Balance):
			print("\tInsufficient Balance.");
		else:
			Balance-=withdraw_amount;
			print(f"Updated Balance: {round(Balance,3)}shs.");
def deposit():
		global Balance;
		print(f"\tCurrent Balance: {round(Balance,3)}shs");
		deposit_amount=float(input("Enter amount to deposit:"));
		Balance+=deposit_amount	;
		print(f"Updated Balance: {round(Balance,3)}shs.");
def main():
	while True:
		print("******************HELLO!******************");
		print("**********Welcome to Atm Banking**********");
		print("1.Deposit");
		print("2.Withdraw.");
		print("3.Check Balance.");
		print("4.Exit.");
		option=int(input("Enter preference:"));
		if(option == 1):
			Balance=deposit();
		elif(option == 2):
			Balance=withdraw();
		elif(option == 3):
			check_bal();
		elif(option == 4):
			exit();
			sys.exit(0);
			#break;
		else:
			print("\tInvalid Input.");

main();
	
	