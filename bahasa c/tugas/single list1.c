#include <stdio.h>
#include <stdlib.h>

struct node {
	int data;
	struct node * link;
};

int main(){
	struct node *es;
	struct node *mie;
	struct node *kue;
	
	es = (struct node*)malloc(sizeof(struct node));
	es->data = 45;
	es->link = NULL;
	
	mie = (struct node*)malloc(sizeof(struct node));
	mie->data = 98;
	mie->link = NULL;
	es->link = mie;
	
	mie = (struct node *)malloc(sizeof(struct node));
	mie->data = 3;
	mie->link = NULL;
	es->link->link = mie;
	
	while (es != NULL){
		printf("%d \n", es->data);
		es = es-> link;
	}
	
	return 0;
}