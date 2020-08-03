#include<iostream>
using namespace std;
int main()
{
	int d,t;
	float c;
	cout<<"请输入里程：";
	cin>>d;
	if (d>10)
	  c=6+(10-2)*1.8+(d-10)*1.8*1.5;
	else
	  if (d>2)
	    c=6+(d-2)*1.8;
	  else
	    c=6;
	cout<<"请输入时间：";
	cin>>t;
	d=d+(t/3)*1;
	cout<<"您共需付："<<c<<"元";
}
