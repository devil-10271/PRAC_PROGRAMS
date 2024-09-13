#include "iostream"

using namespace std;

int main()
{
    int a=5;
    int *b = &a;
    int** c= &b;
    int*** d=&c;


    cout<<"The value of a : "<<a<<endl;
    cout<<"The address of a : "<<&a<<endl;
    cout<<"The address_of(a) is store in b : "<<b<<endl;
    cout<<"The address_of(a) is store in b : "<<&b<<endl;
    cout<<"The address_of(address_of(b)) is store in c : "<<c<<endl;
    cout<<"The address_of(address_of(b)) is store in c : "<<&c<<endl;
    cout<<"The address_of(address_of(address_of(c))) is store in d : "<<d<<endl;
    cout<<"The value_of(address_of(address_of(address_of(d)))) is store in d : "<<***d<<endl;
    return 0;
}