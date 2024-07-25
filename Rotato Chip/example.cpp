#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	string user_Input;
	int length = 0, i = 0;

	cout << "Enter the string to encode" << endl;
	getline(cin, user_Input);

	length = user_Input.length();
	for (i = 0; i < length; i++)
	{
		if (((user_Input[i] >= 65) && (user_Input[i] <= 77)) || ((user_Input[i] >= 97) && (user_Input[i] <= 109)))
		{
			user_Input[i] = user_Input[i] + 13;
		}
		else if (((user_Input[i] >= 78) && (user_Input[i] <= 90)) || ((user_Input[i] >= 110) && (user_Input[i] <= 122)))
		{
			user_Input[i] = user_Input[i] - 13;
		}
		else
		{
			//Do Nothing
		}
	}
	
	cout << user_Input << endl;
	return 0;
}
		
