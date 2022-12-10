#include<stdio.h>
int main()
{
  int i,t,a[10],n,m,s,j=0,b[10];
  printf("\n Masukan Ukuran Array : \n");
  scanf("%d" ,&n);
  printf("\n Masukan Element Array : \n");
  for(i=0;i<n;i++)
  {
    scanf("%d",&a[i]);
  }
  printf("\n Hasilnya : ");
  for(i=0;i<n;i++)
  {
    printf("\n  a [%d] = %d ",i,a[i]);
  }
  printf("\nMasukan posisi yang ingin di update : \n");
  scanf("%d",&t);
  printf("\nMasukan nilai yang ingin di update : \n");
  scanf("%d",&s);
  for(i=0;i<n;i++)
  {
    if(i==t)
    {
       a[i]=s;
    }
  }
  printf("\nUbah element :");
  for(i=0;i<n;i++)
  {
    printf("\n a[%d] = %d",i,a[i]);
  }
  return 0;
}