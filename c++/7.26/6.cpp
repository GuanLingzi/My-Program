#include<iostream>
using namespace std;
int main()
{
	int i,x,max,a;
	cout<<"������Ҫ���뼸������";
	cin>>a;
	cout<<"������ֵ��";
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
