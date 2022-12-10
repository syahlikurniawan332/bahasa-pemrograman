//menampilkan jumlah hari tiap bulan
#include <stdio.h>
main(){
	int hari[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
	int i;
	for(i=0;i<12;i++){
		printf("jumlah hari pada bulan ke %d = %d hari\n",(i+1),hari[i]);
	}
}