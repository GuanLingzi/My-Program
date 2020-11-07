#include<iostream>
using namespace std;
int main()
{
	int i=1000;
	while (i%3!=2||i%5!=4||i%7!=6)
    i++;
	cout<<i;
}
