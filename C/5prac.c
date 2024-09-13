#include"stdio.h"
#include"conio.h"

int main(){
    int i=0,j=0;
    char s1[]="i am a ",s2[]="boy good";
    char s3[1000];

    for(i=0;s1[i]!='\0';i++){
        s3[i]=s1[i];
    }
    s3[i]=' ';
    j=i;
    for (i=0;s2[i]!='\0';i++){
        s3[j]=s2[i];
        j++;
    }
    s3[j]='\0';

    printf("%s",s3);

    return 0;

}