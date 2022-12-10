#include <stdio.h>

main()
{
	//Deklaras dan inisialisasi VAriabel
	int L[10] = {20,15,22,14,12,10,19,18,16}, x=10, flag=0, i;
	
	for(i=0;i<10;i++)
	{
		if(x == L[i])
		{
			flag = 1;
			break;
		}
	}
	if(flag == 1)
	{
		printf("Data ditemukan \n");
		printf("Data yang dicari berada di indek : %d", i);
	}
	else
		printf("Data tidak ditemukan");
}
