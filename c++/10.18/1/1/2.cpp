#include<iostream>
#include<string>
using namespace std;
int main()
{
    const int I=100;
    string sx,sy;
    int lx,ly,l,i,x[I]{0},y[I]{0},z[I],c=0;
    getline(cin,sx);
    getline(cin,sy);
    lx=sx.length();
    ly=sy.length();
    for (i=0;i<lx;i++)
        x[lx-1-i]=sx[i]-'0';
    for (i=0;i<ly;i++)
        y[ly-1-i]=sy[i]-'0';
    l = ly>lx?ly:lx;
    for (i=0;i<l;i++)
    {
        z[i]=x[i]+y[i]+c;
        if (z[i]>=10)
        {
            z[i]-=10;
            c=1;
        }
        else
            c=0;
    }
    if (c==1)
        cout<<c;
    for (i=l-1;i>=0;i--)
        cout<<z[i];
}
