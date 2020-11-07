#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int i,j,a[11],n;
	for (i=1;i<11;i++)
	  a[i]=i;
	i=1;
	cout<<"第"<<setw(3)<<i<<"次位置"<<":";
	for (j=1;j<11;j++)
	  cout<<a[j]<<" ";
  cout<<endl;
  for (i=2;i<=10;i++)
  {
  	for (j=0;j<=10;j++)
  	  a[j]=a[j+1];
	  a[10]=a[0];
	  cout<<"第"<<setw(3)<<i<<"次位置"<<":";
	  for (j=1;j<=10;j++)
	    cout<<a[j]<<" ";
    cout<<endl;
	}
}
