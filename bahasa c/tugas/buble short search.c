#include <conio.h>
main(){
	int a[4];
	int i, n;
	
	printf("masukan size array yang mau di entry = \n");
	scanf("%d",&n);
	for(i=0;i<n;i++){
		printf("masukan elemen array = \n");
		scanf("%d",&a[i]);
	}
	printf("elemen array yang diimputkan\n");
	for(i=0; i<n; i++){
		for(j=0; j<n-1; j++){
		if(a[j]>a[j+1]])
			x=a[j];
			a[j]=a[j+1];
			a[j+1]=x;
	}
	}
}