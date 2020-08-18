#include<iostream>
using namespace std;
int main()
{
	unsigned long long f1,f2,f3,i; 
	f1=1;
	f2=f1;
	cout<<f1<<endl<<f2<<endl;
	for (i=3;i<=90;i++)
	{
		f3=f1+f2;
		cout<<(double)f1/f2<<endl;
		f1=f2;
		f2=f3;
	}
}
