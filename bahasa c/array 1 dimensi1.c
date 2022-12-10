#include <stdio.h>
main(){
	int a[10];
	int i;
	for(i=0;i<10;i++){
		printf("masukan nilai ke-%d :",(i+1));
		scanf("%d",&a[i]);
	}
	printf("\n");
	for(i=0;i<10;i++){
		printf("nilai ke- %d : %d",(i+1),a[i]);
	}
}