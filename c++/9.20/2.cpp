#include<iostream>
using namespace std;
int main()
{
	int b,s,g,shu,count=0;
	for (b=1;b<=7;b++)
	  for (s=0;s<=7;s++)
	    for (g=1;g<=7;g+=2)
	    {
	    	shu=b*100+s*10+g;
	    	cout<<shu<<" ";
	    	count++;
			}
	cout<<endl;
	cout<<"¸öÊý£º"<<count; 
}
