#include<iostream>
using namespace std;
int main()
{
	float height,weight,bmi;
	cout<<"身高（米）:";
	cin>>height;
	if (height<0.4||height>3)
	{
		cout<<"身高值不合法！"<<endl;
		return -1 ;
	}
	cout<<"体重（公斤）：";
	cin>>weight;
	if (weight<1||weight>1000)
	{
		cout<<"体重值不合法！"<<endl;
		return -1;
	}
	bmi=weight/(height*height);
	cout<<"您的BMI指数是："<<bmi<<endl;
	if (bmi<18.5)
	  cout<<"偏瘦"<<endl;
	else if (bmi<24)
	  cout<<"正常"<<endl;
	else if (bmi>28)
	  cout<<"偏胖"<<endl;
	else if (bmi<40)
	  cout<<"肥胖"<<endl;
	else
	  cout<<"极重度肥胖"<<endl;
	system("pause");
}
