#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	double a,b,x,y,z;
	cout<<"请输入四个正整数（从前往后依次是:";
	cout<<"供x亿人生活a年或又可供y亿人生活b年";
	cout<<"用空格分隔 x>y,a<b,ax<by,各整数均不大于10000):";
	cin>>x>>a>>y>>b;
	z=((y*b-x*a)/(b-a));
	printf("%.2lf\n",z);
	return 0;
}
