#include<iostream>
using namespace std;
int main()
{
	unsigned long long a,b,t;
	cout<<"����������������";
	cin>>a>>b;
	t=a;
	while (t%a!=0||t%b!=0)
	{
		t++;
	}
	cout<<t;
}
