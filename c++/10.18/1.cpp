#include<iostream>
using namespace std;
int main()
{
    const int n=8;
    int a[n],i,j,t,b,c;
    for (b=0;b<n;b++)
      cin>>a[b];
    for (i=0;i<n-1;i++)
      for (j=n-1;j>i;j--)
        if (a[j]<a[j-1])
        {
            t=a[j];
            a[j]=a[j-1];
            a[j-1]=t;
        }
    for (c=0;c<n;c++)
      cout<<a[c]<<' ';
}
