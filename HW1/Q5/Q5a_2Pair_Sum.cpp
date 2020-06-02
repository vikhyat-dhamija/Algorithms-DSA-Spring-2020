#include <iostream>
#include<stdlib.h>

using namespace std;

int main()
{
	int input[] = { -1,-2,-3,0,4,3,2,1,6,7,-6 };

	//size of the array
	int n = sizeof(input) / sizeof(int);

	//sorting of the array using the insertion sort

	//Insertion sort
	//Same procedure I used in the Binary serach method of 3 sum N2 Log N method
	//There I have given the detailed theory that how this program executes the insertion sort

	int key;

	for (int i = 1; i < n; i++)
	{
		key = input[i];

		for (int k = i - 1; k >= 0; k--)
		{
			input[k + 1] = input[k];

			if (input[k] <= key)
			{
				input[k + 1] = key;
				break;
			}
			else if (k == 0)
				input[k] = key;

		}
	}

	//
	int left = 0;
	int right = n - 1;

	int start = input[left];

	int count = 0;
	
	double counter = 0;

	while (left < right)
	{
		
		counter++;

		if ((input[left] + input[right]) == 0)
		{
			count++;
			cout << input[left] << "\t" << input[right] << endl;
			left++;
			right--;
		}
		else if ((input[left] + input[right]) > 0)
		{
			right--;
		}
		else
		{
			left++;
		}

	}

	// Printing of the count of the number of pairs summing to zero

	cout << "The number of the two number combinations where sum is equal to 0 are :" << count << endl;

	cout << "The value of the counter measuring the complexity of the algorithm after the sorting is : " << counter << endl;

	

}
