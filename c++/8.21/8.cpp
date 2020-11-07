#include<iostream>
using namespace std;
int main()
{
	char c;
	int a,b,i,j;
	cout<<"请输入行数、列数以及是否空心（是 Y 否 N）：";
	cin>>a>>b>>c;
	for (i=1;i<=a;i++)
	{
		for (j=1;j<=b;j++)
		  if (c=='Y'&&1<i&&i<a&&j>1&&j<b)
		    cout<<" ";
      else
        cout<<"*";
    cout<<endl;
	}
}
