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
		cout<<"������У�";
		cout<<"1.���� 2.ʯͷ 3.��"<<endl;
		cin>>n;
		if (n<1||n>3)
		  cout<<"������1-3���˾���Ч��"<<endl;
		else
		  switch ((m-n+3)%3)
		  {
		  	case 1:cout<<"�����Ӯ��"<<endl; countm++; break;
		  	case 0:cout<<"ƽ�֣�"<<endl; countx++; break;
		  	case -1:cout<<"��Ӯ��"<<endl; countn++; break;
			}
	}
	cout<<endl;
	cout<<"--------------------------------"<<endl;
	cout<<"|"<<"�����Ӯ��"<<countm<<"                   "<<"|"<<endl;
	cout<<"|"<<"��Ӯ��"<<countn<<"                       "<<"|"<<endl;
	cout<<"|"<<"ƽ�ּ���Ч��"<<countx<<"                 "<<"|";
} 
