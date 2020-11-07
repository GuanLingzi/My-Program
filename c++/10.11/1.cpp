#include<iostream>
using namespace std;
int main()
{
	int a[5],n;
	for (int i=0;i<5;i++)
	{
		cout<<i<<"号成绩：";
		cin>>a[i];
	}
	cout<<"输入学号0-4：";
	cin>>n;
	if (n>=0 && n<5)
	  cout<<a[n];
  else
    cout<<"输入的学号不存在！";
}
