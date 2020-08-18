#include<iostream>
using namespace std;
int main()
{
	int i,n,m;
	float ans;
	n=m=0;
	cout<<"请输入：";
	cin>>i;
	while (i!=-1)
	{
		n+=i;
		m++;
		cout<<"请输入：";
		cin>>i;
	}
	if (m!=0)
	{
	ans=(float)n/m;
	cout<<ans; 
  }
  else
    cout<<"班上无学生"; 
}
