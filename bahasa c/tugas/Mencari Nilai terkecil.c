#include <stdio.h>

int main()
{
	int L[10] = {20,15,22,14,12,10,24,19,18,16};
	int min=999;
	int i;
	
	for(i=0;i<10;i++)
	{
		if(L[i]<min)
		{
			min = L[i];
		}
	}
	
	printf("Nilai terkecil adalah: %d", min);
}
