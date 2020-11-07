#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	double in;
	cout<<"输入一个浮点数：";
	cin>>in;
	cout<<fixed<<setprecision(12)<<in;
}
