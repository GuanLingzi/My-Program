#include<iostream>
using namespace std;
int main()
{
	char c;
	int a,b,i,j;
	cout<<"�����������������Լ��Ƿ���ģ��� Y �� N����";
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
