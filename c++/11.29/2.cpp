#include<iostream>
using namespace std;
int main()
{
    const int I=9;
    int m,n;
    int A[2][I][I]={0};
    cin>>m>>n;
    A[0][I/2][I/2]=m;
    for (int d=1;d<=n;d++)
    {
        for (int i=0;i<I;i++)
            for (int j=0;j<I;j++)
                if (A[0][i][j]>0)
                    for (int x=-1;x<=1;x++)
                        for (int y=-1;y<=1;y++)
                            if (x==0&&y==0)
                                A[1][i+x][j+y]+=2*A[0][i][j];
                            else
                                A[1][i+x][j+y]+=A[0][i][j];
        for (int i=0;i<I;i++)
            for (int j=0;j<I;j++)
            {
                A[0][i][j]=A[1][i][j];
                A[1][i][j]=0;
            }
    }
    for (int i=0;i<I;i++)
    {
        for (int j=0;j<I;j++)
            cout<<A[0][i][j]<<'\t';
        cout<<endl;
    }
}
