#include<iostream>
using namespace std;
int main()
{
	int m,n,r;
	cout<<"�����룺";
	cin>>m>>n;
	if (m>=n)
	{ 
	r=m%n;
	while (r!=0)
	{
		m=n;
		n=r;
		r=m%n;
		cout<<"("<<m<<","<<n<<")";
	}
	cout<<n;
  }
  else
    cout<<"��������������";
}
