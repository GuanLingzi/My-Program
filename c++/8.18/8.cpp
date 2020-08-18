#include<iostream>
using namespace std;
int main()
{
	int t,i;
	t=i=0;
	while (1)
	{
		t=t+1;
		i=i+3;
		if (i>=17)
    {
    	cout<<t;
			break;
		}
		else
		{
			t=t+1;
			i=i-1;
		}
	}
}
