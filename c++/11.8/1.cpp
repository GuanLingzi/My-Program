#include<iostream>
using namespace std;
int main()
{
    int naihuang,xiaobai,huihui,huahua;
    bool tj[4];
    for (naihuang=1;naihuang<=4;naihuang++)
        for (xiaobai=1;xiaobai<=4;xiaobai++)
            for (huihui=1;huihui<=4;huihui++)
            {
                huahua=10-naihuang-xiaobai-huihui;
                if (naihuang*xiaobai*huihui*huahua==1*2*3*4)
                {
                    tj[0]=((naihuang==1)+(xiaobai==4)+(huihui==3)+(huahua==2)==2);
                    tj[1]=((xiaobai==1)+(naihuang==4)+(huihui==2)+(huahua==3)==2);
                    tj[2]=((xiaobai==4)+(naihuang==3)==1);
                    tj[3]=((naihuang==1)+(huahua==4)+(xiaobai==3)+(huihui==2)==2);
                    if (tj[0]&&tj[1]&&tj[2]&&tj[3])
                    {
                        cout<<"花花："<<huahua<<endl;
                        cout<<"奶黄："<<naihuang<<endl;
                        cout<<"灰灰："<<huihui<<endl;
                        cout<<"小白："<<xiaobai<<endl;
                        break;
                    }
                }
            }
}

