#include "stdio.h"
#include "stdlib.h"
#include "math.h"
int main()
{
	int num,num1,num2;
	num=13;
	num1=43;
	printf("Before swap: Num:%d\t Num1:%d\n",num,num1);
	num2=num;
	num=num1;
	num1=num2;
	printf("After swap:  Num:%d\t Num1:%d\n",num,num1);
	num=(num+num1);
	num1=(num-num1);
	num=(num-num1);
	printf("Second After swap: Num:%d\t Num1:%d\n",num,num1);
	return EXIT_SUCCESS;
	}
