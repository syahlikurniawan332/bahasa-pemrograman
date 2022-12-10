#include<stdio.h>
#include<stdlib.h>

struct node
{
	 int data;
    struct node*nextPtr;
};
   
struct node*firstNode;
void createNodeList(int number0fNodes);
void insertAtBeginning0fNodeList(int data);
void displayNodeList();

int main()
{
	int number0fNodes;
	int data;
	
	printf("Input nomor nodes : ");
	scanf("%d", &number0fNodes);
	
	createNodeList(number0fNodes);
	
	printf("\nMasukkan data di list :\n");
	displayNodeList();
	
	printf("\nInput data untuk insert di awal list :");
	scanf("%d", &data);
	
	insertAtBeginning0fNodeList(data);	
	printf("\ndata setelah di insert :\n");
	displayNodeList();
	
	return 0;
}

void createNodeList(int number0fNodes)
{
    struct node*newNode;
    struct node*tempNode;
    int nodeData;
    int nodeCtr;
    
    firstNode=(struct node*)malloc(sizeof(struct node));
    
    if(firstNode == NULL)
   {
   	printf("Memory can not be allocated.");
   }
    else
    {
        printf("Input data node1:");
        scanf("%d",&nodeData);
        
        firstNode->data = nodeData;
        firstNode->nextPtr = NULL;
        
        tempNode = firstNode;
        
        for(nodeCtr = 2; nodeCtr <= number0fNodes; nodeCtr++)
        {
        	newNode = (struct node*)malloc(sizeof(struct node));
        	
        	if(newNode == NULL)
        	{
        		printf("Memory can not be allocated.");
        		break;
        	}
        	else
        	{
        		printf("input data node %d :", nodeCtr);
        		scanf("%d", &nodeData);
        		
        		newNode->data = nodeData;
        		newNode->nextPtr = NULL;
        		
        		tempNode->nextPtr = newNode;
        		tempNode = tempNode->nextPtr;
        	}
        }
   	}
}
void insertAtBeginning0fNodeList(int data)
        {
        	struct node *newNode;
        	
        	newNode = (struct node*)malloc(sizeof(struct node));
        	
        	if(newNode == NULL)
        	{
        		printf("Memory can not be allocated.");
       		}
       		else
       		{
       			newNode->data = data;
       			newNode->nextPtr = firstNode;     			
       			firstNode = newNode;
       		}
}

void displayNodeList()
{
	struct node*tempNode;
	
	if(firstNode == NULL)
	{
		printf("No data found in the list.");
	}
	else
	{
		tempNode = firstNode;		
		while (tempNode != NULL)
		{
			printf("Data =%d\n", tempNode->data);
			tempNode = tempNode->nextPtr;
	}
}
}
