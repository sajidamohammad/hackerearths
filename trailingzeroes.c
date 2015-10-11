#include<stdio.h>

int zero_count(int n)
{
	int count=0,i;
	for (i=5;n/i>=1;i=i*5)
	{
	count+=n/i;		
	}
return count;
}

int main(){
	int n;
	scanf("%d",&n);
	printf("%d\n",zero_count(n));
}
