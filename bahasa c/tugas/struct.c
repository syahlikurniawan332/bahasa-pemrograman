#include <stdio.h>
struct siswa
{
	int id;
	char nama[20];
	float nilai;
};

main(){
	struct siswa s1;
	
	printf("masukan detail s1 = \n");
	printf("id : ");
	scanf("%d", &s1.id);
	printf("nama : ");
	scanf("%s",&s1.nama);
	printf("nilai : ");
	scanf("%f",&s1.nilai);
	
	printf("\n detail s1 \n");
	printf("id : %d\n nama siswa : %s\n nilai : %f",s1.id,s1.nama,s1.nilai);
}