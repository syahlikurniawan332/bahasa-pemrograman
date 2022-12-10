#include <stdio.h>

main()
{
	//mendeskripsikan array dan variabel i
	int i,j,n,temp;
	int array[]={30,10,40,20,50};
	for(i=0;i<n;i++)
	scanf("%d",&array[i]);
	
	for(i=1;i<n;i++)
	{
		temp=array[i];
		j=i-1;
		while((temp<array[j])&&(j>=0))
		{
			array[j+1]=array[j];
			j=j-1;
		}
		array[j+1]=temp;
	}
	printf("urutkan array : \n");
	for(i=0;i<n;i++)
	printf("%d",array[i]);
}