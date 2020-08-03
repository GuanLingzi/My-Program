#include<iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;
int main()
{
	int n,a;
	srand(time(0));
	a=rand()%10+1;
	cout<<"ÇëÊäÈëºÅÂë£¨10-1£©£º";
	cin>>n;
	if (n==a)
	  cout<<"ÖÐ½±£¡";
	else
	  cout<<"Î´ÖÐ½±"; 
}
