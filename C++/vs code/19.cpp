#include"stdio.h"
#include"conio.h"
#include"stdlib.h"
#include<iostream>


using namespace std;
int m1(int a,int b,int c);
int m1(int a,int b);


int main(){
    int a=m1(12,12);
    int b=m1(2,2,2);
    cout<<a<<endl;
    cout<<b<<endl;
}


int m1(int a,int b,int c){
    return (a*b*c);
}

int m1(int a,int b){
    return a*b;
}