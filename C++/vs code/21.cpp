#include"iostream"
#include"stdio.h"
#include"conio.h"
#include"string.h"

using namespace std;


class employee{
    private:
    string surname,name,fathername;
    public:
    void b(string pname,string psname,string pfname);
    };

void employee :: b(string pname,string psname,string pfname){
    cout << "The employee name is : "<< psname<<" "<<pname<<" "<<pfname<<endl;
}

int main(){
    employee e01;
    e01.b("sahil","devani","maheshbhai");
    return 0;
}