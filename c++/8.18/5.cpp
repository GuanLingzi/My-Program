#include<iostream>
#include<cstdlib>
#include<time.h>
using namespace std;
int main()
{
	const int MAX=4;
	int m,n,countm,countn,countx;
	countm=countn=0;
	for (int i=0;i<MAX;i++)
	{
		do
		{
		  cout<<"请你出招：";
		  cout<<"1.剪刀 2.石头 3.布"<<endl;
	    cin>>n;
	  }while(n<1||n>3);
		m=rand()%3+1;
	  switch ((m-n+3)%3)
	  {
  	  case 1:cout<<"计算机赢！"<<endl; countm++; break;
  	  case 0:cout<<"平局！"<<endl; countx++; break;
  	  default:cout<<"你赢！"<<endl; countn++; break;
		}
	}
	cout<<endl;
	cout<<"--------------------------------"<<endl;
	cout<<"|"<<"计算机赢："<<countm<<"                   "<<"|"<<endl;
	cout<<"|"<<"你赢："<<countn<<"                       "<<"|"<<endl;
	cout<<"|"<<"平局："<<countx<<"                       "<<"|";
} 
