def gcd(int_1,int_2):
	min= int_1 if (int_2 > int_1) else int_2;
	greatest_factor=1;
	for factor in range(1, (min+1)):
		if ((int_1 % factor)==0 )and ((int_2 % factor)==0):
			greatest_factor=factor;
	return greatest_factor	;
def get_int(name):
	num=(int(input(f"Enter {name} integer:")))
	return num 	;
def main():
	num_1=get_int("First");
	num_2=get_int("Second");
	factor=(gcd(num_1,num_2));
	print(f"The Greatest common factor: {factor}");
main();