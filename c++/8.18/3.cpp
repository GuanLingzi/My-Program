#include<iostream>
using namespace std;
int main()
{
	char x;
	for (x='A';x<='D';x++)
	  if ((x!='A')+(x=='C')+(x=='D')+(x!='D')==3)
	  {
	  	cout<<"С͵�ǣ�"<<x;
	  	break;
		}
}
