#include<iostream>
using namespace std;
int main()
{
	int i,n,m;
	float ans;
	n=m=0;
	cout<<"�����룺";
	cin>>i;
	while (i!=-1)
	{
		n+=i;
		m++;
		cout<<"�����룺";
		cin>>i;
	}
	if (m!=0)
	{
	ans=(float)n/m;
	cout<<ans; 
  }
  else
    cout<<"������ѧ��"; 
}
