#include<iostream>
using namespace std;
int main()
{
	int i;
	float s=1;
	for (i=600;i<=2020;i++)
	{
		s=s*1.03;
		cout<<i<<' '<<s<<endl; 
	}
}
