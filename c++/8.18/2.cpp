#include<iostream>
using namespace std;
int main()
{
	long long a,n;
	n=2;
	a=1;
	for (int i=1;i<=30;i++)
	{
		cout<<a<<endl;
		a+=n;
		n*=2;
	}
} 
