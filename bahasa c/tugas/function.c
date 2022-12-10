#include <stdio.h>
int minimum(int x, int y)
{
	int kecil;
	if(x<y)
	kecil=x;
	else
	kecil=y;
	return kecil;
}
main()
{
	int a,b,c;
	printf("membandingan nilai variabel mana yang lebih kecil\n");
	printf("masukan nilai 1 : \n");
	scanf("%d",&a);
	printf("masukan nilai 2 : \n");
	scanf("%d",&b);
	c=minimum(a,b);
	printf("nilai terkecil adalah : %d",c);
}

