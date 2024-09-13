// for find the length of string


#include"conio.h"
#include"stdio.h"
#include"string.h"
#include"stdlib.h"

int main(){
    char stri[]="hello world";
    int length=0;
    for ( int i=0;stri[i]!='\0';i++){
        length++;
    }
    printf("%s",stri);
    printf("\n%d",length);
    
    return 0;
}