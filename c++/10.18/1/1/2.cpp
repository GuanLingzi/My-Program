#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    int i,j,m,n,count=0,A[100][100],B[100][100];
    float sim;
    cin>>m>>n;
    for (i=0;i<m;i++)
        for (j=0;j<n;j++)
            cin>>A[i][j];
    for (i=0;i<m;i++)
        for (j=0;j<m;j++)
            cin>>B[i][j];
    for (i=0;i<m;i++)
        for (j=0;j<m;j++)
            if (A[i][j]==B[i][j])
                count++;
    sim=count*100.0/(m*n);
    cout<<fixed<<setprecision(2)<<sim;
}
