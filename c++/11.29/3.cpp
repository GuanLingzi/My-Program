#include<iostream>
using namespace std;
int main()
{
    const int I=9;
	const int N=5;
    int m,n;
    int A[N][I][I]={0};
    cin>>m>>n;
    A[0][I/2][I/2]=m;
    for (int d=1;d<=n;d++)
        for (int i=0;i<I;i++)
            for (int j=0;j<I;j++)
                if (A[d-1][i][j]>0)
                    for (int x=-1;x<=1;x++)
                        for (int y=-1;y<=1;y++)
                            if (x==0&&y==0)
                                A[d][i+x][j+y]+=2*A[d-1][i][j];
                            else
                                A[d][i+x][j+y]+=A[d-1][i][j];
    for (int i=0;i<I;i++)
    {
        for (int j=0;j<I;j++)
            cout<<A[n][i][j]<<'\t';
        cout<<endl;
    }
}
