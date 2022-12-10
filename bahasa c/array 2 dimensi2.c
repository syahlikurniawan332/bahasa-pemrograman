#include <stdio.h>
int main(void){
	//deklarasi dan inisialisasi array dua dimensi
	//dengan jumlah elemen baris = 3
	//dan jumlah elemen kolom = 2
	int matriks[3][2] = {{1,2},{3,4},{5,6}};
	//mendeklarasi variabel untuk
	//indeks perulangan
	int i,j;
	
	printf("\t==================================");
	printf("\n\t=== TAMPIL MATRIK ORDO 3x2 ===\n");
	//menampilkan matriks
	printf("\t menampilkan matrik contoh\n");
	for(i=0;i<3;i++){
		for(j=0;j<2;j++){
			printf("%d ",matriks[i][j]);
		}
		printf("\n");
	}
	return 0;
}