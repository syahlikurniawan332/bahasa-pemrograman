#include <stdio.h>

main()
{
	//mendeskripsikan array dan variabel i
	int a[] = {1,2,3,4,5,7};
	int i;
	//menampilkan keterangan sebelum di insertion
	printf("Elemen sebelum array: \n");
	//perulangan untuk menampilkan array
	for(i=0; i<6; i++)
	{
		//perintah menampilkan array
		printf("Nilai [%d] : %d \n", i,a[i]);
	}
	//perulangan menampil array setelah di insertion
	for(i=5;i>=4; i--)
	{
		a[i+1] = a[i];
	}
	//index yang akan ditambah 
	a[5] = 20;
	
	printf("\n");
	//menampilkan perintah keterangan sesudah di insertion
	printf("Elemen array sesudah di insert : \n");
	for(i=0; i<7; i++)
	{
		printf("Nilai [%d] = %d \n", i, a[i]);
	}
}
