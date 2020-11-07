#include<iostream>
using namespace std;
int main()
{
	int i;
  for (i=1;(i+6)%13!=0||(i-6)%12!=0;i++);
  cout<<i;
}
