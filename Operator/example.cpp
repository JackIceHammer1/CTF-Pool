#include <iostream>
using namespace std;

int main()
{
	int op1 = 0, op2 = 0, sum = 0, product = 0;
	
	cout << "Enter two numbers to add and multiply together:" << endl;
	cin >> op1 >> op2;
	
	sum = op1 + op2;
	product = op1 * op2;
	cout << "The sum of " << op1 << " and " << op2 << " is: " << sum << endl;
	cout << "The product of " << op1 << " and " << op2 << " is: " << product << endl;
	
	return 0;
}
