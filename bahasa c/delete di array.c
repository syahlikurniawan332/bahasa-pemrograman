#include <stdio.h>
int main(){
	int nama[10],p,c,n;
	printf("masukan nomor elemen di array \n");
	scanf("%d", &n);
	printf("masukan %d element \n", n);
	for (c=0;c<n;c++)
	scanf("%d", &nama[c]);
	printf("pilih lokasi elemen yang ingin di hapus \n");
	scanf("%d", &p);
	if(p >= n+1)
	printf("tidak mungkin menghapus \n");
	else
	{
		for (c = p - 1; c < n - 1; c++ )
		nama[c] = nama[c+1];
		printf("array yang dihasilkan : \n");
	
		for (c=0;c<n-1;c++)
		printf("%d\n", nama[c]);
	}
	return 0;
}