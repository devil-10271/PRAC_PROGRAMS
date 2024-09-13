#include "iostream"

using namespace std;

int main()
{
    int age;
    cout << "Enter the age : ";
    cin >> age;
    if (age >= 18 && age <= 100)
    {
        cout << "elegible for party"<<endl;
    }

    else if (age >= 120)
    {
        cout << "wrong age"<<endl;
    }
    else
    {
        cout << "not eligible for party"<<endl;
    }

    switch (age)
    {
    case 18:
        printf("eligible for party");
        break;

    default:
        cout << "not eligible for party";
        break;
    }

    return 0;
}