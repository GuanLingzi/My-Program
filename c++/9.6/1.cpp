#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int i,j,n;
	cin>>n;
	for (i=1;i<=n;i++)
	{
		cout<<setw(21-i);
		for (j=1;j<=2*i-1;j++)
		  cout<<'*';
    cout<<endl;
	}
}
