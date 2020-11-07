#include<iostream>
using namespace std;
int main()
{
	long long m,n,t;
	cin>>m>>n;
	if (m<n)
	{
		t=m;
		m=n;
		n=t;
	}
	t=n;
	while (n%t||m%t)
	  t--;
  cout<<t<<endl;
}
