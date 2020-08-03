#include<iostream>
using namespace std;
int main()
{
	double n=1,sum=0,i;
	for (i=1;i<=64;i++)
	{
		n*=2;
		sum+=n;
		cout<<i<<' '<<n<<endl;
	}
	cout<<"×ÜÊý£º"<<sum;
}
