#include<iostream>
using namespace std;
int main()
{
	int time=0,count=1,teacher,nike,glair;
	bool flag;
	teacher=nike=glair=0;
	do
	{
		flag=0;
		time++;
		if (teacher<9)
		{
			teacher++;
			flag=1;
		}
		if (nike<9&&time%2==0)
		{
			nike++;
			flag=1;
		}
		if (glair<9&&time%4==0)
		{
			glair++;
			flag=1;
		}
		if (flag)
		  count++;
	} while (teacher+nike+glair<9*3);
	cout<<count;
}
