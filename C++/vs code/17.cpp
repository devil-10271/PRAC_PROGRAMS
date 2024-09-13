#include"iostream"

using namespace std;



inline int product(int a,int b){
    return a*b;
}
int main(void){
    int x=6,y=12;
    cout<<"product of 12 and 6 is : "<<product(x,y);
    return 0;
}