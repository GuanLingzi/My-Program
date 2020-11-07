#include<iostream>
using namespace std;
int main()
{
	int i,cishu;
	bool a[10];
	for (int i=0;i<10;i++)
    a[i]=true;
	for (cishu=1;cishu<1000;cishu++)
	{
		i=(i+cishu)%10;
		if (i==0)
	    i=10;
	  a[i]=false;
	}
	for (int i=0;i<10;i++)
	{
		if (a[i])
		  cout<<i<<endl;
	}
}
