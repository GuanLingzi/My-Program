#include<iostream>
using namespace std;
int main()
{
	int i=1,m,n,r;
	cout<<"输入两个正整数：";
	cin>>m>>n;
	r=m%n;
	if (m%n!=0)
	{
		cout<<"0.";
    while (i<=100)
	  {
		  cout<<(r*10)/n;
		  r=(r*10)%n;
		  i++;
	  }
	}
	else
	{
		cout<<m/n;
	}
}
