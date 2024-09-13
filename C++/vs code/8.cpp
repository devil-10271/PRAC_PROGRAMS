#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int i = 0;
    const int five = 5;
    for (int i = 0; i < five; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            cout << "*";
        }
        cout << "\n";
    }
    for (int i = five; i > 0; i--)
    {
        for (int j = i; j > -1 + 1; j--)
        {
            cout<<"*";
        }
        cout<<'\n';
    }
}