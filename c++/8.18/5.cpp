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
		  cout<<"������У�";
		  cout<<"1.���� 2.ʯͷ 3.��"<<endl;
	    cin>>n;
	  }while(n<1||n>3);
		m=rand()%3+1;
	  switch ((m-n+3)%3)
	  {
  	  case 1:cout<<"�����Ӯ��"<<endl; countm++; break;
  	  case 0:cout<<"ƽ�֣�"<<endl; countx++; break;
  	  default:cout<<"��Ӯ��"<<endl; countn++; break;
		}
	}
	cout<<endl;
	cout<<"--------------------------------"<<endl;
	cout<<"|"<<"�����Ӯ��"<<countm<<"                   "<<"|"<<endl;
	cout<<"|"<<"��Ӯ��"<<countn<<"                       "<<"|"<<endl;
	cout<<"|"<<"ƽ�֣�"<<countx<<"                       "<<"|";
} 
