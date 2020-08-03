#include<iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;
int main()
{
	int n,a,b;
	srand(time(0)); 
	a=rand()%90+10;
	b=rand()%90+10;
	cout<<a<<'+'<<b<<'=';
	cin>>n;
	if (n==a+b)
	  cout<<"ÕýÈ·";
	else
	  cout<<"´íÎó"; 
 } 
