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

	//Variables used in the algorithm

	int left  = 0;
	int right = n - 1;

	int start = input[left];

	int count = 0;

	double counter = 0;


	//Algorithm for find the three number sum equal to 0
	//Just the modification with the 2 sum method of this way
	//Here what we have done is that we moved linearly to pick one number and then found the corresponding 
	// negative number in rest of the array 
	// so two loops hencea quadratic algorithm
	//first loop above 
	for (int i = 0; i <= (n - 3); i++)
	{
		left = i + 1;
		right = n - 1;
		// second loop concretely explained in the pdf in the 2 sum case i.e. the q5_a problem the logic behind it
		while (left < right) // till the left is less than that of the right index
		{
			counter++; // complexity counter increment for measuring the complexity

			if ((input[left] + input[right]) == (-input[i])) // when number found
			{
				count++; // increase pair count
				cout << input[left] << "\t" << input[right] <<"\t"<<input[i]<< endl; // printing the pair values
				left++; // increasing the left side
				right--; // decreasing the right side
			}
			else if ((input[left] + input[right]) > (-input[i])) // when the sum becomes gretar than the test value decrease the right side
			{
				right--;
			}
			else
			{
				left++; // when the opposite of above the left side increases
			}

		}
	}

	// Printing of the count of the number of pairs summing to zero and the complexity counter

	cout << "The number of the three number combinations where sum is equal to 0 are :" <<  count << endl ;

	cout << "The value of the counter measuring the complexity of the algorithm after the sorting is : " << counter << endl;

}


