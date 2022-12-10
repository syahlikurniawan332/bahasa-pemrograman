#include <stdio.h>

main()
{
	//mendeskripsikan array dan variabel i
	int i,j,n,temp;
	printf("masukan jumlah array : ");
	scanf("%d",&n);
	int array[n];
	
	printf("masukan elemen array : \n");
	for(i=0;i<n;i++)
	scanf("%d",&array[i]);
	
	for(i=1;i<n;i++)
	{
		temp=array[i];
		j=i-1;
		while((array[j]<temp)&&(j>=0))
		{
			array[j+1]=array[j];
			j--;
		}
		array[j+1]=temp;
	}
	printf("urutkan array : \n");
	for(i=0;i<n;i++)
	printf("%d",array[i]);
}