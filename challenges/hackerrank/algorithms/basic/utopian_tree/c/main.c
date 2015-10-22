/*
    type: challenge solution
    theme: basic
    sub-theme: basic
    name: utopian tree
    author of code: Darya @dar-drozdova Drozdova

*/

#include <stdio.h>

int main(void)
{

    int tests;
    scanf("%d", &tests);
    int k;
    for(k = 0; k<tests; k++){
        int a;
        scanf("%d",&a);
        int i;
        int height=1;
        for (i=0;i<a;i++){
            if (i%2==0)
            {
                height*=2;
            }
            else {
                height+=1;
            }
        }
        printf("%d",height);
    }

    return 0;
}
