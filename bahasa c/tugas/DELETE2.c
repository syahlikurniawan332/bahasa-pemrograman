#include <stdio.h>

main()
{
	int a[] = {1,2,3,4,5};
	int i,j;
	
	printf("Sebelum DELETE: \n");
	
	for(i=0; i<5; i++)
	{
		printf("Nilai [%d] : %d \n", i,a[i]);
	}
	
	//perulangan untuk melkukan pergeseran ke kiri
	j=2;
	while(j<5)
	{
		a[j-1] = a[j];
		j = j+1;
		
	}
	
	
		

	
	printf("\n");
	
	printf("Sesduah DELETE: \n");
	for(i=0; i<4; i++)
	{
		printf("Nilai [%d] = %d \n", i, a[i]);
	}
}
