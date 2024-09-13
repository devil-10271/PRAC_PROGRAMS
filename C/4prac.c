// this code for compare strings

#include"stdio.h"
#include"conio.h"

int main(){

    char s1[]="hello world",s2[]="Hello world";
    int same=0;
    int ls1=0,ls2=0;
    for(int i=0;s1[i]!='\0';i++){
        ls1++;
    }
    for(int i=0;s2[i]!='\0';i++){
        ls2++;
    }

    if( ls1!=ls2){
        printf("string are not equal");
    }
    else{
        for(int i=0;s1[i]!='\0';i++){
            if(s1[i]!=s2[i]){
                break;
            }
            else{
                same=1;
            }
        }
    }

    if(same==0){
        printf("string are not equal");
    }
    else{
        printf("string are equal..");
    }
    

    printf("\n\n%d %d",ls1,ls2);
    return 0;
}