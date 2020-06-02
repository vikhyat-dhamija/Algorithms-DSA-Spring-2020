// q1_ds.cpp : This file contains the 'main' function. Program execution begins and ends there.
// The naive cubic order of growth algorithm for the three sum problem

#include <iostream>
#include <fstream>
#include <stdlib.h>

//Macro for determining the size of the array for the storage of elements from the file and then running the algorithm

#define N 4192

using namespace std;

int main()
{
	int input[N];//array used for putting the elements for further algorithm

	fstream source;// fstream object

    source.open("4192int.txt");// opening the file please change the number ahead and the macro for running the program for different data set

	if (!source)//just checking whether the file is properly opened or not
	{
		cout << "File could not be opened" << endl;
		exit(1);
	}

	int temp , count=0 , r_count=0, key=0;
	int test = 0 ;// variables used in the program
	//Note test is the variable for checking the sum of the pairs to certain value in our program has been considered 0

	while (source >> temp)//sucking in the data elemnets from the file 
	{
		input[count++] = temp;
	}

	double complexity_counter = 0; // complexity counter in double as the value can be large

	//Three loops for forming the pair and note that first loop for 2 less than N values band second 1 less than N and the third till the last
	//The above is done for forming 3 pair combinations
	for (int i = 0; i < (N-2); i++)
	{
		for (int j = i+1; j < (N-1); j++)
		{
			for (int k = j+1; k < N; k++)
			{
				if ((input[i] + input[j] + input[k]) == test)//check whether the sum is as desired
					r_count++;
				complexity_counter++;
			}

		}
	}

	cout << "The value of the proxy complexity counter for " <<N<<" size dataset is "<< complexity_counter;//displaying the complexity counter

	source.close();// file closed 
}

