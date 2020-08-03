#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	int bai,shi,ge,i;
	for (i=100;i<1000;i++)
	{
		bai=i/100;
		shi=(i/10)%10;
		ge=i%10;
		if (pow(bai,3)+pow(shi,3)+pow(ge,3)==i)
		  cout<<i<<"  ";
	}
}
