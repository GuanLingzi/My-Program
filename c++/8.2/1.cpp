#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	int n,i;
	bool flag;
	cout<<"���������֣�";
	cin>>n;
	flag=true;
	if (n<2)
	  cout<<"�Ȳ���������Ҳ���Ǻ���";
	else 
	{
    for (i=2;i<=sqrt(n);i++)
	    if (n%i==0)
	    {
	  	  flag=false;
	  	  break;
		  }
	  if (flag)
      cout<<"������";
    else
      cout<<"��������"; 
  }
} 
