#include<iostream>
using namespace std;
int main()
{
	int d,t;
	float c;
	cout<<"��������̣�";
	cin>>d;
	if (d>10)
	  c=6+(10-2)*1.8+(d-10)*1.8*1.5;
	else
	  if (d>2)
	    c=6+(d-2)*1.8;
	  else
	    c=6;
	cout<<"������ʱ�䣺";
	cin>>t;
	d=d+(t/3)*1;
	cout<<"�����踶��"<<c<<"Ԫ";
}
