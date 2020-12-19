#include<iostream>
using namespace std;
int main()
{
	const int I=9;
	int m,n;
	int A[I][I]={0},B[I][I]={0};
	cin>>m>>n;
	A[I/2][I/2]=m;
	for (int d=1;d<=n;d++)
	{
		for (int i=0;i<I;i++)
			for (int j=0;j<I;j++)
				if (A[i][j]>0)
					for (int x=-1;x<=1;x++)
						for (int y=-1;y<=1;y++)
							if (x==0&&y==0)
								B[i+x][j+y]+=2*A[i][j];
							else
								B[i+x][j+y]+=A[i][j];
		for (int i=0;i<I;i++)
			for (int j=0;j<I;j++)
			{
				A[i][j]=B[i][j];
				B[i][j]=0;
			}
	}
	for (int i=0;i<I;i++)
	{
		for (int j=0;j<I;j++)
			cout<<A[i][j]<<'\t';
		cout<<endl;
	}
}
