#include<iostream>
#include<string>
using namespace std;
int main()
{
    char s;
    string str1,str2;
    getline(cin,str1);
    str2="";
    for (int i=0;i<str1.length();i++)
    {
        s=str1[i];
        if ((s>='a' && s<='z')||(s>='A' && s<='Z'))
        {
            s++;
            if ((s>'Z' && s<'a')||s>'z')
                s-=26;
        }
        str2+=s;
    }
    cout<<str2<<endl;
}
