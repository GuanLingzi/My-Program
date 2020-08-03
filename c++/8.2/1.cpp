#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	int n,i;
	bool flag;
	cout<<"请输入数字：";
	cin>>n;
	flag=true;
	if (n<2)
	  cout<<"既不是质数，也不是合数";
	else 
	{
    for (i=2;i<=sqrt(n);i++)
	    if (n%i==0)
	    {
	  	  flag=false;
	  	  break;
		  }
	  if (flag)
      cout<<"是质数";
    else
      cout<<"不是质数"; 
  }
} 
