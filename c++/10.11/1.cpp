#include<iostream>
using namespace std;
int main()
{
	int a[5],n;
	for (int i=0;i<5;i++)
	{
		cout<<i<<"�ųɼ���";
		cin>>a[i];
	}
	cout<<"����ѧ��0-4��";
	cin>>n;
	if (n>=0 && n<5)
	  cout<<a[n];
  else
    cout<<"�����ѧ�Ų����ڣ�";
}
