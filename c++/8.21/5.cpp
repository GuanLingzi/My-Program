#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	double x,y;
	long long a,b,m,n,r;
	cout<<"������һ��С����";
	do
	{
		cout<<"x=";
		cin>>x;
	} while (x<=0||x>=1);
	a=1;
	y=x;
	while (fabs(y-(int)y)>1e-10)
	{
		a*=10;
		y=x*a;
	}
	b=y;
	cout<<b<<'/'<<a<<endl;
	m=a;
	n=b;
	r=m%n;
	while (r!=0)
	{
		m=n;
		n=r;
		r=m%n;
	}
	cout<<"������Ϊ��";
	cout<<b/n<<'/'<<a/n<<endl;
}
