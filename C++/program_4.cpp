#include <iostream>
using namespace std;
class average
{
public:
    static int cal_average(int x, int y, int z)
    {
        return (x + y + z / 3.0);
    }
};
int main()
{
    int x, y, z;
    cout << "enter three number : ";
    cin >> x >> y >> z;

    cout << "the average is " << average::cal_average(x, y, z);
}