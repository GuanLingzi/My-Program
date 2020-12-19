#include<iostream>
using namespace std;
int main()
{
    int i,n,sum[2],ans;
    sum[0]=0;
    sum[1]=1;
    cin>>n;
    for (i=1;i<=n;i++)
    {
        sum[1]*=i;
        while (sum[1]%10==0)
        {
            sum[1]/=10;
            sum[0]++;
        }
        sum[1]%=1000;
    }
    ans=sum[0];
    cout<<ans;
}

