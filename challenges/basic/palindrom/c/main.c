#include <stdio.h>
int modul(int a){
    if (a<0){
        return -a;
    }
    else {
        return a;
    }
}

int main(void)
{

    char *s = "aecdb";
    int f=0;
    int i;
    int r;
    for (i=0;i<2;i++){
        r=s[i]-s[4-i];
        f+=modul(r);
    }
    printf("%d",f);
    return 0;
}

