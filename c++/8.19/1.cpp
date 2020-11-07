#include<iostream>
using namespace std;
int main()
{
	int num,a;
	cout<<"请输入十进制数：";
	cin>>num;
	while (num!=0)
	{
		a=num%2;
		cout<<a;
		num=num/2;
	}
}
