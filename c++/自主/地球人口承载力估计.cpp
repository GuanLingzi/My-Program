#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	double a,b,x,y,z;
	cout<<"�������ĸ�����������ǰ����������:";
	cout<<"��x��������a����ֿɹ�y��������b��";
	cout<<"�ÿո�ָ� x>y,a<b,ax<by,��������������10000):";
	cin>>x>>a>>y>>b;
	z=((y*b-x*a)/(b-a));
	printf("%.2lf\n",z);
	return 0;
}
