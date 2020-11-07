#include<iostream>
using namespace std;
int main()
{
	int num=0;
	float n,sumone,sum=0.0;
	bool flag=true;
	while (flag)
	{
		sumone=0;
		do
		{
			cin>>n;
			if (n==-1)
			  flag=false;
	    else
	      sumone+=n;
	  }while (n!=0 && n!=-1);
	  cout<<sumone<<endl;
	  if (sumone!=0)
	  	num++;
  	sum+=sumone;
	}
	cout<<sum<<"  "<<num;
}
