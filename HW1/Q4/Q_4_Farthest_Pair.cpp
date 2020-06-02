// farthest_pair_problem.cpp : This file contains the 'main' function. Program execution begins and ends there.


#include <iostream>

using namespace std;

#define N 10
// number of values in the array

int main()
{
	double input[N] = { 1,2,3,4,5,6,7,8,9,10 }; // Hard Coded array and for other input values need to change the value of the array

	double counter = 0;

	if (N == 1)// when the array has 1 value then array has pne value
		cout << "List has only one value";
	else if (N == 2) // when array value 2 
		cout << "Farthest distance is " << abs(input[0] - input[1]) << " with pair " << input[0] << " and " << input[1] << endl;
	else
	{ // else max min algorithm in the linear complexity for finding the farthest distance between any two points which is the distance between the max and min numbers only

		double max, min;
		
			if (input[0] > input[1]) // first we initialise the maximum and minimum values with first two values
			{  // Lower in min and higher in max
				max = input[0];
				min = input[1];
		    }
			else
			{
				max = input[1];
				min = input[0];
			}
			// Then we lineraly in one loop move across the whole array  
			for (int i = 2; i < N; i++)
			{ //when the number is greater than max then change max 

				counter++;

				if (input[i] > max)
				{
					max = input[i];
				}
				else if (input[i] < min) // else if the number is the number is less than min then change min
				{
					min = input[i];
				}

			}
			cout << "Farthest distance is " << (max-min) << " with pair of numbers " << max << " and " << min << endl;

			// Distance is calculated by taking the differenece between the minimum and max

			cout << "The value of the counter measuring the complexity of the algorithm is : " << counter << endl;

	}
}


