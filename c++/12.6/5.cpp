#include<iostream>
using namespace std;
int ans;
int max(int x,int y)
{
	if (x>y)
		return x;
	else
		return y;
}
void fun()
{
	int i,a[5];
	for (i=0;i<5;i++)
		cin>>a[i];
	ans=a[0];
	ans=max(ans,a[1]);
    ans=max(ans,a[2]);
    ans=max(ans,a[3]);
    ans=max(ans,a[4]);
}
int main()
{
	fun();
	cout<<ans;
}
