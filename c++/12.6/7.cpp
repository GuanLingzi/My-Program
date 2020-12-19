#include<iostream>
using namespace std;
bool wanshu(int n)
{
	int sum=0;
	for (int i=1;i<n;i++)
		if (n%i==0)
			sum+=i;
	return sum==n;
}
int main()
{
	int ans=0;
	for(int i=1;i<=100;i++)
		if (wanshu(i))
		{
			cout<<i<<' ';
			ans++;
		}
	cout<<ans<<endl;
}
