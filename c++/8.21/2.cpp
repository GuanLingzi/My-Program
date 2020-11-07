#include<iostream>
using namespace std;
int main()
{
	int num=0,nike,glair,n=0;
	nike=glair=0;
	do
	{
		nike++;
		if (nike>20)
		  nike=1;
    glair++;
    if (glair>30)
      glair=1;
    if (nike==glair)
      num++;
    n++;
	} while (n<1000);	
	cout<<num;
}
