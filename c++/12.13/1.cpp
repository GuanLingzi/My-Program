#include<iostream>
using namespace std;
int binary()
{
	
}
bool palindrome(int m)
{
	int temp=m,n=0;
	binary();
	while(temp)
	{
		n=n*10+temp%10;
		temp/=10;
	}
	return(n==m);
}
int main()
{
	cin>>m;
	a=palindrome(n);
	
}
