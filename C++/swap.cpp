
#include <iostream>
using namespace std;

int main()
{
	int a, b;
	cout<<("Enter the two numbers : \n");
	cin>>a>>b);
	cout<<("Before swapping A is : %d and B is %d \n", a,b); 

	int temp;
	temp = a;
	a = b;
	b = temp;

	cout<<("After swapping A is : %d and B is : %d \n", a,b);
	return 0;
}
