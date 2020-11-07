#include<iostream>
using namespace std;
int main()
{
  int count=0,x;
  cout<<"输入一个整数：";
  cin>>x;
  while (x!=1)
  {
  	cout<<x<<" "<<"-->"<<" ";
  	if (x%2==1)
  	  x=x*3+1;
		else
		  x=x/2;
    count++;
	}
	cout<<x<<endl<<"--------------------------------"<<endl<<count;
}
