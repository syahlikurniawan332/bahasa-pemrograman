#include <stdio.h>

int main()
{
	int L[10] = {70,68,67,45,25,23,17,15,14,12};
	int k; 				//Indeks tengah
	int i;				//Indeks awal
	int n = 10;			
	int j = n-1;		//Indeks akhir
	int x = 67;			//Data yang dicari
	int flag = 0;
	
	for(i=0;i<=n;i++)
	{
		k= (i+j)/2;
		
		if(L[k] == x)
		{
			flag = 1;
			break;
		}
		
		for(i=0;i<j;i++)
		{
			k= (i+j)/2;
			
			if(L[k] > x)
			{
				if(L[k] < x)				
					i=k;	
			}
			else{
				j=k;
			}
		}
	}
	
	if(flag == 1)
	{
		printf("Data ditemukan \n");
		printf("Berada dindeks %d", k);
	}
	else{
		printf("Data tidak ditemukan");
	}
}
