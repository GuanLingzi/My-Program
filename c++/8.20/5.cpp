#include<iostream>
using namespace std;
int main()
{
	unsigned long long n,sum=0,a;
	cout<<"����һ��������";
  cin>>n;
	do
	{
		a=n%10;
		sum+=a;
		n/=10; 
  } while (n!=0);
  cout<<sum;
}
