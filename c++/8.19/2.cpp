#include<iostream>
using namespace std;
int main()
{
	int m,n,t=0;
	cout<<"请输入两个正整数：";
	cin>>m>>n;
	while (m>n)
	{
		m-=n;
		t++;
	}
	cout<<t<<"  "<<m;
}
