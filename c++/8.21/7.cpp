#include<iostream>
#include<iomanip> 
using namespace std;
int main()
{
	int i,j,a,b,s;
	cout<<"������������������";
	cin>>a>>b;
	for (i=1;i<=a;i++)
	{
		cout<<setw(21-b);
		for (j=1;j<=2*i-1;j++)
		  cout<<'*';
    cout<<endl;
	}
}
