#include<iostream>
using namespace std;
int main()
{
    int a[6][3],n,i;
    for (i=1;i<=5;i++)
    {
        cout<<i<<"号成绩(语文-数学-英语）:";
        cin>>a[i][0]>>a[i][1]>>a[i][2];
    }
    while (true)
    {
        cout<<"输入学号：";
        cin>>n;
        if (n>0&&n<=5)
            cout<<n<<"号成绩："<<"语文："<<a[n][0]<<"数学："<<a[n][1]<<"英语："<<a[n][2]<<endl;
        else
            cout<<"没有此学号的成绩"<<endl;
    }
}
