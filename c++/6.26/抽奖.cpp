#include<iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;
int main()
{
	int n,a;
	srand(time(0));
	a=rand()%10+1;
	cout<<"��������루10-1����";
	cin>>n;
	if (n==a)
	  cout<<"�н���";
	else
	  cout<<"δ�н�"; 
}
