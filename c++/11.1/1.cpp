#include<iostream>
#include<string>
using namespace std;
int main()
{
    char s;
    string str1,str2="";
    int i;
    getline(cin,str1);
    for (i=0;i<str1.length();i++)
    {
        s=str1[i];
        if ((s>='a'&&s<='z')||(s>='A'&&s<='Z'))
        {
            s+=3;
            if ((s>'Z'&&s<'a')||s>'z')
                s-=26;
        }
        str2+=s;
    }
    cout<<str2;
}
