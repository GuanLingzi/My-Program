#include<iostream>
using namespace std;
int main()
{
	int num,m,n;
	cout<<"���������֣�";
	cin>>num;
	n=num;
	for (m=0;n>0;)
	{
		m=m*10+n%10;
		n=n/10;
	}
	if (m==num)
	  cout<<"�ǻ�����";
  else
    cout<<"���ǻ�����";
}
