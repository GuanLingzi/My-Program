#include<iostream>
using namespace std;
int main()
{
	int i=1;
	double n1,n2;
	n1=1-0.01;
	n2=1+0.01;
	cout<<n1<<"  "<<n2<<endl;
	while (i<=15)
	{
		n1=n1*n1;
		n2=n2*n2;
		cout<<i<<"  "<<n1<<"  "<<n2<<endl;
		i++;
	}
}
