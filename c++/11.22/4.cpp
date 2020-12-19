#include<iostream>
using namespace std;
int main()
{
    int i,j;
    float score[3][5],avg[3],sum;
    for (i=0;i<3;i++)
        for (j=0;j<5;j++)
            cin>>score[i][j];
    for (i=0;i<3;i++)
    {
        sum=0;
        for (j=0;j<5;j++)
            sum+=score[i][j];
        avg[i]=sum/5;
    }
    for (i=0;i<3;i++)
        cout<<avg[i]<<' ';
}

