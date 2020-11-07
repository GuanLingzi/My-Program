#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int cock,hen,chick;
	cout<<setw(5)<<"¹«¼¦"<<setw(5)<<"Ä¸¼¦"<<setw(5)<<"Ð¡¼¦"<<endl;
	for (cock=1;cock<=20;cock++)
	  for (hen=1;hen<=33;hen++)
		  for (chick=1;chick<=100;chick++)
		    if ((cock+hen+chick==100)&&(cock*5+hen*3+chick/3==100))
		      cout<<setw(5)<<cock<<setw(5)<<hen<<setw(5)<<chick<<endl;
}
