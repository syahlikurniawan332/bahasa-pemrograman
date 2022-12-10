#include <stdio.h>

int main()
{
	int a[5] = {10,30,20,50,40};
	int cari=20;
	int i;
	
	for(i=0; i<5; i++)
	{
		printf("Nilai [%d]: %d \n", i, a[i]);
	}
	
	for(i=0; i<a; i++)
	{
		if(a[i] == cari)
		{
			printf("Nilai yang anda cari berada di index: [%d]", i);
			break;
		}
	}
}
