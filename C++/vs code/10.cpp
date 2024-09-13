#include"iostream"

using namespace std;

int main (){
    int num;
    cout<<"Enter the number for table : ";
    cin>>num;
    int i=1;
    do{
        cout<<num<<" x "<<i<<" = "<<i*num<<endl;
        i++;
    }while(i<=10);
    return 0;
}