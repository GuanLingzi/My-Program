#include<iostream>
using namespace std;
int main()
{
	int i;
	for(i=1;i<=20;i++)
	{
		if(i%7==0||i%10==7)
		    continue;
		cout<<i<<endl;
	}
}
