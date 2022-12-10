#include <stdio.h>
void minimum(int x,int y)
{
	int k;
	if(x<y)
	k=x;
	else
	k=y;
	printf("nilai terkecil adalah : %d",k);
}
main()
{
	int a,b,k;
	printf("membandingan nilai variabel mana yang lebih kecil\n");
	printf("masukan nilai 1 : \n");
	scanf("%d",&a);
	printf("masukan nilai 2 : \n");
	scanf("%d",&b);
	minimum(a,b);
}