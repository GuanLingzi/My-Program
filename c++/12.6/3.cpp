#include<iostream>
using namespace std;
void show(int n)
{
	for (int i=0;i<n;i++)
		cout<<"*";
	cout<<endl;
}
int main()
{
	int i,n;
	cout<<"行数：";
	cin>>n;
	for (i=1;i<=n;i++)
		show(i);
}

