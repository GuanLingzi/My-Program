#include<iostream>
using namespace std;
int main()
{
	float height,weight,bmi;
	cout<<"��ߣ��ף�:";
	cin>>height;
	if (height<0.4||height>3)
	{
		cout<<"���ֵ���Ϸ���"<<endl;
		return -1 ;
	}
	cout<<"���أ������";
	cin>>weight;
	if (weight<1||weight>1000)
	{
		cout<<"����ֵ���Ϸ���"<<endl;
		return -1;
	}
	bmi=weight/(height*height);
	cout<<"����BMIָ���ǣ�"<<bmi<<endl;
	if (bmi<18.5)
	  cout<<"ƫ��"<<endl;
	else if (bmi<24)
	  cout<<"����"<<endl;
	else if (bmi>28)
	  cout<<"ƫ��"<<endl;
	else if (bmi<40)
	  cout<<"����"<<endl;
	else
	  cout<<"���ضȷ���"<<endl;
	system("pause");
}
