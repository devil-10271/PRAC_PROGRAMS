#include "iostream"

using namespace std;

union add
{
    float a = 1.1;
    int b;
};

int main()
{
    union add ok;
    // one.a=1000;
    ok.b = 222;
    cout << ok.b<<endl;
    cout << ok.a;
    return 0;
}