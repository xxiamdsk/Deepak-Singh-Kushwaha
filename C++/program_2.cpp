#include <iostream>
#include <math.h>
using namespace std;
class triangle
{
public:
    int area(int a, int b, int c);
    int perimeter(int a, int b, int c);
};
int triangle::area(int a, int b, int c)
{
    float s = (a + b + c) / 2.0, A = sqrt(s * (s - a) * (s - b) * (s - c));
    cout << "area of triangle=" << A;
}
int triangle::perimeter(int a, int b, int c)
{
    cout << "perimeter of triangle=" << a + b + c;
}
int main()
{
    triangle tr;
    int side1 = 4, side2 = 5, side3 = 6;
    tr.area(side1, side2, side3)<<endl;
    tr.perimeter(side1, side2, side3);
}