#include <stdio.h>
int main(){
	int nama[100],p,c,n,value;
	printf("masukan nomor untuk menentukan ukuran array \n");
	scanf("%d", &n);
	printf("masukan %d element \n", n);
	for (c=0;c<n;c++)
	scanf("%d", &nama[c]);
	printf("pilih lokasi indeks yang di tambah \n");
	scanf("%d", &p);
	printf("masukan nilai yang benar \n");
	scanf("%d", &value);
	for (c = n - 1; c >= p - 1; c-- )
	nama[c+1] = nama[c];
	printf("array yang dihasilkan : \n");
	
	for (c=0;c<=n;c++)
	printf("%d\n", nama[c]);
	
	return 0;
}