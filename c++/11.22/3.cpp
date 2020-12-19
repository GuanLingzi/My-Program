#include<iostream>
using namespace std;
int main()
{
    int a[4][4],i,j,n=0;
    for (i=0;i<4;i++)
        for (j=0;j<4;j++)
            cin>>a[i][j];
    for (i=0;i<4;i++)
        n+=a[i][i];
    cout<<n;
}
