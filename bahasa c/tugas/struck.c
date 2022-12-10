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
	
	printf("masukan data siswa \n");
	for(i=0;i<10;i++){	
	printf("masukan id siswa : ");
	scanf("%d",&sis[i].id);
	printf("masukan nama siswa :");
	scanf("%s",&sis[i].nama);
	printf("masukan nilai siswa :");
	scanf("%f",&sis[i].nilai);
	printf("\n");
	}
	printf("\ndetail data siswa : \n");
	for(i=0;i<10;i++)
	{
		printf("id siswa : %d nama siswa : %s nilai siswa : %f",sis[i].id,sis[i].nama,sis[i].nilai);
	}
}