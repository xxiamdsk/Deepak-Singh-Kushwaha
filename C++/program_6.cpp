#include <iostream>
using namespace std;
class factorial
{
public:
    int num;

    int getdata()
    {
        cout << "enter your number : ";
        cin >> num;
        display();
    }

    int facto()
    {
        int fact = 1;
        for (int i = 1; i <= num; ++i)
        {
            fact *= i;
        }
        cout << "Factorial of " << num << " = " << fact;
    }

    int display()
    {
        facto();
    }
};

int main()
{
    factorial f;

    f.getdata();
}