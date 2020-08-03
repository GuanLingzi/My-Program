#include<iostream>
using namespace std;
int main()
{
	int num,m,n;
	cout<<"请输入数字：";
	cin>>num;
	n=num;
	for (m=0;n>0;)
	{
		m=m*10+n%10;
		n=n/10;
	}
	if (m==num)
	  cout<<"是回文数";
  else
    cout<<"不是回文数";
}
