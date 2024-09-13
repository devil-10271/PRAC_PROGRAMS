#include"iostream"

using namespace std;

int fact(int fac);

int main(){
    int a;
    cout<<"enter the number : ";
    cin>>a;
    int ans=fact(a);
    cout<<"factorial of "<<a<<" : "<<ans;
    return 0;
}

int fact(int fac){
    if(fac==1||fac==0){
        return 1;
    }
    else{
        return fac*fact(fac-1);
    }
}