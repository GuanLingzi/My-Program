//
// Created by mac on 2020/12/20.
//

#include<iostream>
using namespace std;
void show(int count)
{
    for (int i=0;i<count;i++)
        cout<<"*";
    cout<<endl;
}
int main()
{
    int n=4;
    show(1);
    show(2);
    show(n-1);
    show(n);
}