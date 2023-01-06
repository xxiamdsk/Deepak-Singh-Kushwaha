#include <iostream>
#include <math.h>
using namespace std;
class triangle
{
public:
    int area(int a, int b, int c);
    int perimeter(int a, int b, int c);
    int display();

    triangle(int a, int b, int c)
    {
        area(a, b, c);
        perimeter(a, b, c);
    }
};
int triangle::area(int a, int b, int c)
{
    float s = (a + b + c) / 2.0, A = sqrt(s * (s - a) * (s - b) * (s - c));
    cout << "area of triangle=" << A << endl;
}

int triangle::perimeter(int a, int b, int c)
{
    cout << "perimeter of triangle=" << a + b + c;
}

int main()
{
    triangle tr(side1, side2, side3);
    int side1 = 4, side2 = 5, side3 = 6;
}