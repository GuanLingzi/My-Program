#include<iostream>
using namespace std;
int main()
{
	unsigned long long f0=0,f1=1,f2,i,n;
	cout<<"ÊäÈëÊý×Ö£º";
	cin>>n;
	for (i=2;i<n;i++)
	{
		f2=f0+f1;
		cout<<f2<<endl;
		f0=f1;
		f1=f2;
	}
}
