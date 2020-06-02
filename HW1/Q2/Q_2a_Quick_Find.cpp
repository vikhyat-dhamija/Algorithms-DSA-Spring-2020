// quickfind.cpp : This file contains the 'main' function. Program execution begins and ends there.

#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <time.h>

using namespace std;

#define N 8192
//define the size of the array 

double complexity_counter; // xcomplexity counter for measuring the complexity

//Find function which basically finds that whether the two elemnets are connected or not
bool find(int * p,int x, int y)
{
	complexity_counter++; //to meaure how many times the comparison operation for find happens
	return (p[x] == p[y]); // just return whether the label of the two elements is same or not

}

//For the union of two elements
void unions(int*p,int x, int y)
{
	int a = p[x];
	int b = p[y];
	
	// labels of the two elements to be connected are picked up 
	
	//Then all the elements with source element label are found out and their label is changed with that of the destination eleemnt
	for (int i = 0; i < N; i++)
		{
			complexity_counter++;
			if (p[i] == a)
				p[i] = b;
		}

}




int main()
{
	
	int pair[N];
	//initialising the array
	for (int i = 0; i < N ; i++)
	{
		pair[i] = i;
	}

	fstream source;

	source.open("8pair.txt");// opening of the file 

	if (!source)// check whether the file properly opened or not
	{
		cout << "File could not be opened" << endl;
		exit(1);
	}

	//variable declarations
	int element1, element2, temp, count = 0;;

	//quick find method for the solution
	//sucking of elements from the file
	while (source >> temp)
	{
		element1 = temp;
		source >> element2;
		
		count++;
		//first find called and if not connected union is called and the pair is printed with now connected key word proving they are connected now
		if (!find(pair, element1, element2))
		{
			unions(pair, element1, element2);
			cout << element1 << "\t" << element2 << "\t" << endl;
		}
		
	}
	
	cout << "The complexity of the quick find algorithm for " << count << " size data set is " << complexity_counter << endl;
	
}

