#include<iostream>
using namespace std;
int main()
{
	int i=0,i2=0,a,b,n,f,s;
	cout<<"����������������";
	cin>>a>>b;
	cout<<"С�����λ��";
	cin>>s;
	if (a>b)
	{
		f=a/b;
		cout<<f<<".";
		if (a%b!=0)
		{
	    while (i<=s)
		  {
		    a=a*10;
		    n=a/b;
		    cout<<n;
		    a=a%b;
		    i++;
		  }
		}
  }
  if (a<b)
  {
  	cout<<"0.";
  	while (i<=s)
  	{
  		a=a*10;
  		n=a/b;
  		cout<<n;
  		b=a%b;
  		i++;
		}
	}
}
