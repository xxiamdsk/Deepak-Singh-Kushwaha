#include <iostream>
using namespace std;

class Complex
{
private:
    int real, imag;

public:
    Complex(int r=0 , int i=0 )
    {
        real = r;
        imag = i;
    }

    Complex operator+(Complex obj)
    {
        Complex res;
        res.real = real + obj.real;
        res.imag = imag + obj.imag;
        return res;
    }
    int print() { cout << real << " + i" << imag << '\n'; }
};

int main()
{

    int a, b,c,d;
    cout<<"Enter real and imagenary number : " ;
    cin>>a>>b;
    cout<<"Enter real and imagenary number : " ;
    cin>>c>>d;
    
    Complex c1(a,b), c2(c,d);
    Complex c3 = c1 + c2;
    c3.print();
}
