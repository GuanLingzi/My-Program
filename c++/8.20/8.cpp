#include<iostream>
using namespace std;
int main()
{
	int p=1,x=15,sum;
	sum=x;
	cout<<p<<"  "<<x<<"  "<<sum<<endl;
	do
	{
		p+=1;
		x+=2;
		sum+=x;
		cout<<p<<"  "<<x<<"  "<<sum<<endl;
	} while (sum!=312);
	cout<<"--------------------------------"<<endl;
	cout<<x<<"  "<<p;
}
