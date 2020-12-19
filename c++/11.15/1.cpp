#include<iostream>
using namespace std;
int main()
{
    int i,top,k,num;
    bool a[30] {};
    top=0;
    for (i=top,k=0,num=0;num<15;i++)
    {
        if (i>29)
            i=0;
        if (!a[i])
            k++;
        if (k==9)
        {
            a[i]=true;
            k=0;
            num++;
        }
    }
    cout<<"骨头所在的位置：";
    for (i=0;i<30;i++)
        if (!a[i])
            cout<<i<<" ";
}

