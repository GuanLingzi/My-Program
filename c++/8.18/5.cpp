#include<iostream>
#include<cstdlib>
#include<time.h>
using namespace std;
int main()
{
	const int MAX=10;
	int m,n,countm,countn,countx;
	countm=countn=0;
	for (int i=0;i<MAX;i++)
	{
		m=rand()%3+1;
		cout<<"请你出招：";
		cout<<"1.剪刀 2.石头 3.布"<<endl;
		cin>>n;
		if (n<1||n>3)
		  cout<<"请输入1-3，此局无效！"<<endl;
		else
		  switch ((m-n+3)%3)
		  {
		  	case 1:cout<<"计算机赢！"<<endl; countm++; break;
		  	case 0:cout<<"平局！"<<endl; countx++; break;
		  	case -1:cout<<"你赢！"<<endl; countn++; break;
			}
	}
	cout<<endl;
	cout<<"--------------------------------"<<endl;
	cout<<"|"<<"计算机赢："<<countm<<"                   "<<"|"<<endl;
	cout<<"|"<<"你赢："<<countn<<"                       "<<"|"<<endl;
	cout<<"|"<<"平局及无效："<<countx<<"                 "<<"|";
} 
