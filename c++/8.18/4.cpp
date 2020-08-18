#include<iostream>
#include<cstdlib>
#include<time.h>
using namespace std;
int main()
{
	int sum,i,x,y,symbol,ans,n,t;
	sum=0;
	srand(time(0));
	for (i=1;i<=10;i++)
	{
		x=rand()%10;
		y=rand()%10;
		symbol=rand()%2;
		if (x<y&&symbol==1)
		{
			x=t;
			x=y;
			y=t;
		}
		if (symbol==1)
		{
			ans=x-y;
			cout<<x<<"-"<<y<<"=";
			cin>>n;
		}
		if (symbol==0)
		{
			ans=x+y;
			cout<<x<<"+"<<y<<"=";
			cin>>n;
		}
		if (n==ans)
		{
			sum+=10;
			cout<<"correct"<<endl;
		}
		if (n!=ans)
		  cout<<"error"<<endl;
	}
	cout<<"score:"<<sum;
}
