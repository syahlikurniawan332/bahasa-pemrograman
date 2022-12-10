#include <stdio.h>

int main()
{
	int a[5] = {10,20,30,40,50};
	int i;
	
	printf("sebelum di UPDATE!!! \n");
	
	for(i=0; i<5; i++)
	{
		printf("Nilai [%d]: %d \n", i, a[i]);
	}
	
	a[2] = 70;		// Memasukan nilai elemen
	
	printf("\n");
	
	printf("Sesudah di UPDATE!!! \n");
	
	for(i=0; i<5; i++)
	{
		printf("Nilai [%d]: %d \n", i, a[i]);
	}
}
