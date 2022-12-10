#include <stdio.h>

int main()
{
	//deklarasi dan inisialisasi variabel
	int a[5] = {10,30,20,50,40};
	int cari,i,flag=0;
	
	printf("masukan kunci yang ingin di cari : ");
	scanf("%d",&cari);
	for(i=0; i<5; i++)
	{
		if(cari==a[i])
		{
			flag=1;
			break;
		}
	}
	if(flag==1)
		printf("data ditemukan");
	else
		printf("data tidak ditemukan");
}