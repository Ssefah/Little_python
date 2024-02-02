#include "stdio.h"
#include "stdlib.h"
#include "math.h"
int main()
{
	size_t cha,in,dou,vio,floa;
	cha=sizeof(char );
	in=sizeof(int );
	dou=sizeof(double );
	vio=sizeof(void );
	floa=sizeof(float );
	printf("Size of character:%u\n",cha );
	printf("Size of character:%u\n",in);
	printf("Size of character:%u\n",dou);
	printf("Size of character:%u\n",vio);
	printf("Size of character:%u\n",floa);
return EXIT_SUCCESS;
	}
