//memasukan nilai ke array 2 dimensi
#include <stdio.h>
int main(void){
	int i,j,baris,kolom;
	printf("masukan baris : ");
	scanf("%d",&baris);
	printf("masukan kolom : ");
	scanf("%d",&kolom);
	int m[baris][kolom];
	printf("masukan angka ke dalam matriks : ");
	printf("\n");
	
	for(i=0;i<baris;i++){
		for(j=0;j<kolom;j++){
			printf("baris %d kolom %d : ",i+1,j+1);
			scanf("%d",&m[i][j]);
		}
	}

	printf("\t==================================");
	printf("\n\t=== HASIL INPUT NILAI KE MATRIKS ===\n");
	//menampilkan matriks
	printf("\t menampilkan matrik contoh\n");
	for(i=0;i<baris;i++){
		for(j=0;j<kolom;j++){
			printf("\t %d ",m[i][j]);
		}
		printf("\n");
	}
	return 0;
}