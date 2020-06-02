// q1_2_ds.cpp : This file contains the 'main' function. Program execution begins and ends there.


#include <iostream>
#include <fstream>
#include <stdlib.h>

#define N 4192
//as in previous algorithm the N value can be changed as per the dataset used in order to change the size of the array
using namespace std;



int main()
{
	int input[N];// array for input

	fstream source;//fstream source

	source.open("4192int.txt");// opening the desired file the number in the front has to be changed


	if (!source)// if file is not opened
	{
		cout << "File could not be opened" << endl;
		exit(1);
	}

	int temp, count = 0, r_count = 0 , key=0;// variables used
	int test = 0 ;//specific value to which the sum is tested

	while (source >> temp)//sucking the data from the file
	{
		input[count++] = temp;//putting the data in the array
	}

	
	//Insertion sort of complexity O(n^2)

	for (int i = 1; i < N; i++)
	{
		key = input[i]; // Key taken to be put into the shuffled cards

		for (int k = i - 1; k >= 0; k--) // that key pair moves through the already soterd array in front 
		{
			input[k + 1] = input[k];// just start shifting the cards aside 
			
			if (input[k] <= key)//and whenevr it find the card smaller than and equal to the key value card 
			{
				input[k + 1] = key; // just put the key card there and get out of the loop
				break;
			}
			else if (k == 0)  //and when searching for smaller card reaches front then just put the key in the front
				input[k] = key;
			
	    }
	}
	
	int x, mid , flag,low,high  ;// variables used
	double complexity_counter = 0;// counter for calculating the complexity
	
	//Two sum + Binary search to reduce the time taken by algorithm

	for (int i = 0; i < (N-2); i++)// Two loops to form the two pairs
	{
		for (int j = i + 1; j < (N-1); j++)
		{
			
			//Binary Search algorithm
			low = j + 1;//Low 
			high = N - 1;// high

			mid = (low + high) / 2; // Mid of the array made of the low and high

			flag = 0; // flag sets to 0

			while (low <= high) //loop while the low is less than high 
			{
				
				complexity_counter++;// counter for calculating the complexity

				if (input[mid] == (test - (input[i] + input[j]))) // if the desired value is found
				{
					flag = 1;
					break;
				}
				else if (input[mid] > (test - (input[i] + input[j])))//else moves right and left whther the mid value is greater or smaller than the desired number
				{
					high = mid - 1;
				}
				else
				{
					low = mid + 1;
				}

				mid = (low + high) / 2;
			}

			if (flag) r_count++;;	//for calculating the desired number of pairs 

		}
	}
	
	cout << "The value of the proxy complexity counter for " << N << " size dataset is " << complexity_counter;//just display the counter for complexity

	source.close();


}

