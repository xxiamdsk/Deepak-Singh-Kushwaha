#include <iostream>
using namespace std;

int fabo(int num)
{
    int a = 0, b = 1, c = 0;
    cout << a << " ";
    cout << b << " ";
    for (int i = 2; i < num; i++)
    {

        c = a + b;
        cout << c << " ";
        a = b;
        b = c;
    }
}

int main()
{
    int num;
    cout << "enter the terms";
    cin >> num;
    fabo(num);
}