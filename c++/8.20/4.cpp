#include<iostream>
using namespace std;
int main()
{
	float x;
	do
	{
		cout<<"ÇëÊäÈë³É¼¨(0-100)£º";
		cin>>x;
	} while (x<0||x>100);
	cout<<"³É¼¨£º"<<x<<endl;
}
