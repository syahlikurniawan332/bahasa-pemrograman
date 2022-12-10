#include <stdio.h>
struct siswa
{
	int id;
	char nama[20];
	float nilai;
};

main(){
	int i;
	struct siswa sis[2];
	
	printf("masukan data karyawan \n");
	for(i=0;i<2;i++){	
	printf("masukan id : ");
	scanf("%d",&sis[i].id);
	printf("masukan nama :");
	scanf("%s",&sis[i].nama);
	printf("masukan departemen :");
	scanf("%s",&sis[i].departemen);
	printf("masukan jabatan :");
	scanf("%s",&sis[i].jabatan);
	printf("masukan gaji :");
	scanf("%f",&sis[i].gaji);
	printf("\n");
	}
	printf("\ndetail data data karyawan : \n");
	
	for(i=0;i<2;i++)
	{
		printf("id : \n%d nama : \n%s departemen : \n%s jabatan : \n%s gaji : %f",sis[i].id,sis[i].nama,sis[i].departemen,sis[i].jabatan,sis[i].gaji);
	}
}