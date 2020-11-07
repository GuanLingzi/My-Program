#include<iostream>
#include<math.h>
using namespace std;
int main()
{
  double x,y;
	int num;
	cout<<"请输入一个小数（小数位数不超过9位）"<<endl;
  do
  {
  	cout<<"x=";
  	cin>>x;
	} while (x>=1||x<=0);
	num=1;
	do
	{
		num*=10;
		y=x*num;
	} while (fabs(y-(int)y)>1E-9);
	cout<<(int)y;
}
