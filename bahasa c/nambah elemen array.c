#include <stdio.h>
int main(){
	int nama[100]={0};
	int i, x, pos, n = 10;
	for (i=0;i<10;i++)
	nama[i]=i+1;
	for(i=0;i<n;i++)
	printf("%d",nama[i]);
	printf("\n");
	x=38;
	pos=2;
	n++;
	for(i=n-1; i >= pos; i--)
	nama[i]=nama[i-1];
	nama[pos-1]=x;
	for(i=0;i<n;i++)
	printf("%d", nama[i]);
	printf("\n");
	
	return 0;
}