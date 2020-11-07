#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
  char ch;
  bool f=false;
	int num=0;
	while ((ch=getchar())!='\n')
	{
		if (f)
		  if (ch>'0'&&ch<='9')
		    num++;
      else
        break;
    if (ch=='.')
      f=true;
	}
	if (num>0)
	  cout<<num;
  else
    cout<<"输入不正确！";
}
