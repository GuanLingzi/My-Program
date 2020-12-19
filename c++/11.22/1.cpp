#include<iostream>
using namespace std;
int main()
{
    int c[5],b[5],n,i;
    for (i=1;i<=5;i++)
    {
        cout<<i<<"号成绩(语文成绩在前 数学成绩在后）:";
        cin>>c[i]>>b[i];
    }
    while (true)
    {
        cout<<"输入学号：";
        cin>>n;
        if (n>0||n<=5)
            cout<<n<<"号成绩："<<"语文："<<c[n]<<"数学："<<b[n]<<endl;
        else
            cout<<"没有此学号的成绩"<<endl;
    }
}

