#include <iostream>
using namespace std;
class friend_function
{
    int a, b;

public:
    int getdata()
    {
        cout << "Enter the value of a and b : ";
        cin >> a >> b;
    }
    int display()
    {
        cout << "a = " << a << " b = " << b << endl;
    }
    friend int sum(friend_function);
};
int sum(friend_function f)
{
    return f.a + f.b;
}
int main()
{
    friend_function f;
    f.getdata();
    f.display();
    cout << "Sum of a and b is : " << sum(f);
}
 