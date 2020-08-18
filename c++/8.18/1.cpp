#include<iostream>
using namespace std;
int main()
{
	unsigned long long f1,f2,f3,i;
	f1=1;
	f2=f1;
	cout<<f1<<" "<<f2<<" ";
	for (i=3;i<=100;i++)
	{
		f3=f1+f2;
		cout<<f3<<" ";
		f1=f2;
		f2=f3;
	} 
}
