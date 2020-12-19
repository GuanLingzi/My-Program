#include<iostream>
using namespace std;
int main()
{
    const int M=10;
    int i,j,p,n;
    int a[M+1];
    for (i=1;i<=M;i++)
        a[i]=i+1;
    a[M]=1;
    cout<<"n=";
    cin>>n;
    p=M;
    for (i=1;i<=M;i++)
    {
        for (j=1;j<=n-1;j++)
            p=a[p];
        cout<<a[p]<<" ";
        a[p]=a[a[p]];
    }
}

