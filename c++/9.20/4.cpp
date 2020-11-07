#include<iostream>
using namespace std;
int main()
{
	int n,i;
	cin>>n;
	cout<<n<<'=';
	for (i=2;n!=1;i++)
	{
		while (n%i==0)
		{
			cout<<i;
			n/=i;
			if (n!=1)
			  cout<<'*';
		}
	}
}
