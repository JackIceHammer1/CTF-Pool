#include <iostream>
#include <cstring>
using namespace std;

void string_reverse(char string[], int length);

int main()
{
	int i = 0, j = 0, length = 0;
	char plaintext[50];
	
	cout << "Enter a string to encode:" << endl;
	cin.getline(plaintext, 50);
	
	length = strlen(plaintext);
	for (i = 0, j = 1; i < length; i++)
	{
		if ((plaintext[i] != '{') && (plaintext[i] != '}'))
			{
				plaintext[i] = plaintext[i] + j;
			}
		j = j * 2;
	}
	
	string_reverse(plaintext, length);
	
	for (i = 0; i < length; i++)
	{
		cout << plaintext[i]; 
	}
	cout << endl;
	
	return 0;
}
	
void string_reverse(char string[], int length)
{
	int i = 0, j = 0;
	char a;
	j = length - 1;
	for (i = 0; i < (length / 2); i++, j--)
	{
		a = string[i];
		string[i] = string[j];
		string[j] = a;
	}
}
