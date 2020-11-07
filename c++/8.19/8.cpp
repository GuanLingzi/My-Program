#include<iostream>
using namespace std;
int main()
{
	unsigned long long sum=2020,n,i=1;
	cout<<"ÇëÊäÈë£º";
	cin>>n;
	while (i<=n)
	{
		if (i%2==1)
		  sum-=i;
		else
		  sum+=i;
		i++; 
	}
	cout<<sum;
}
