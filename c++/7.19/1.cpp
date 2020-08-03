#include<iostream>
using namespace std;
int main()
{
	int i;
	for (i=1;i<=20;i++)
	{
	cout<<i<<endl;
	  if (i%2==0)
	    cout<<"¶£¶£";
	  if (i%3==0)
	    cout<<"µ±µ±";
	  if (i%2==0||i%3==0)
	    cout<<endl;
	}
}
