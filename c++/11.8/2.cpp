#include<iostream>
using namespace std;
int main()
{
    int a[3],ans=0;
    for (int i=0;i<3;i++)
        cin>>a[i];
    ans+=a[0]*(a[0]>a[1]&&a[0]>a[2]);
    ans+=a[1]*(a[1]>a[0]&&a[1]>a[2]);
    ans+=a[2]*(a[2]>a[0]&&a[2]>a[1]);
    cout<<ans<<endl;
}
