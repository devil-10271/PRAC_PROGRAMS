// for copy string in another string

#include"stdio.h"
#include"conio.h"

int main(){
    char s1[]="my name is sahil",s2[1000];
    int i;
    for(i=0;s1[i]!='\0';i++){
        s2[i]=s1[i];
    }
    s2[i]='\0';

    printf("%s\n",s1);
    printf("%s",s2);
    return 0;
}