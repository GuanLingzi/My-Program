#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    char ch1[1000],ch2;
    int num[26],i,k;
    for (i=0;i<26;i++)
        num[i]=0;
    gets(ch1);
    i=0;
    while (ch1[i]!='\0')
    {
        if (ch1[i]>='a' && ch1[i]<='z')
        {
            k=ch1[i]-'a';
            num[k]++;
        }
        i++;
    }
    for (i=0;i<26;i++)
    {
        ch2='a'+i;
        cout<<ch2<<':'<<num[i]<<" ";
        if (i%5==4)
            cout<<endl;
    }
}
