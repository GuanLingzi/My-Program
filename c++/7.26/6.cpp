#include<iostream>
using namespace std;
int main()
{
	int i,x,max,a;
	cout<<"请输入要输入几个数：";
	cin>>a;
	cout<<"请输入值：";
	cin>>x;
	max=x;
	for(i=2;i<=a;i++)
	{
	  cin>>x;
	  if(x>max)
	    max=x;
	}
	cout<<max;
}
