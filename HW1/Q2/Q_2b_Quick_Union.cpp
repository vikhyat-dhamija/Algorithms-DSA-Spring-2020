// quickunion.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include<ctime>

using namespace std;

#define N 8192
//Size of an array

double complexity_counter; // complexity counter for measuring the complexity

int root(int* p, int x)// function for find the root of an element
{
	int t = x;
	complexity_counter++; // whenever the root function is called and the first access of the array takes place
	while (t != p[t]) //till the label and the element value does not remain same that means that root has not been reached
	{ // because when root is reached then the label and the lement both are same.
		t = p[t]; // getting up the tree
		complexity_counter++; // complexity counter for measuring the complexity
	}

	return t; // return the root element
}

bool long_find(int* p, int x, int y) // here function of find is named long find
{
	return(root(p, x) == root(p, y)); // root of the both elements are found and compared

}

void quickunion(int* p, int x, int y) // root are found and the label of the source root is changed to that of destination root in ordre to make it a sub tree
{
	    int rootx, rooty;

		rootx = root(p, x);
		rooty = root(p, y);
		p[rootx] = p[rooty];


}

int main()
{
	int pair[N];
	int count = 0;

	//initialisation of an array
	for (int i = 0; i < N; i++)
	{
		pair[i] = i;
	}

	fstream source;

	source.open("32pair.txt");

	if (!source)
	{
		cout << "File could not be opened" << endl;
		exit(1);
	}

	int element1, element2, temp;

	//quick union method for the solution

		

	while (source >> temp)
	{
		element1 = temp;
		source >> element2;
		count++;

		// same as in all find union algorithms
		if (!long_find(pair, element1, element2))
		{
			quickunion(pair, element1, element2);
			cout << element1 << "\t" << element2 << "\t" << endl;
		}
		
	}

	cout << "The complexity of the quick find algorithm for " << count << " size data set is " << complexity_counter << endl;
	
}


