#include<iostream>
using namespace std;
int main()
{
	int i,j,ans=0;
	for (i=1;i<=99;i++)
	  for (j=1;j<=i;j++)
	  {
	  	ans++;
	  	if (i==99&&j==9)
	  	  break;
		}
	cout<<ans;
}
