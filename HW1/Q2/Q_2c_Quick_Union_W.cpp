// quickunion_wb.cpp : This file contains the 'main' function. Program execution begins and ends there.


#include <iostream>
#include <fstream>
#include <stdlib.h>
#include<ctime>

using namespace std;

#define N 8192
//size of the array

double complexity_counter; // complexity counter for measuring the complexity

int root_wb(int* p, int x) // root finding algorithms same as that of the quick union as the logic is same 
{
	int t = x;
	complexity_counter++;
	while (t != p[t])
	{
		t = p[t];
		complexity_counter++;
	}

	return t;
}

bool long_find_wb(int* p, int x, int y) // find function is same as that of the quick union as the logic is same 
{
	return(root_wb(p, x) == root_wb(p, y));

}

void quickunion_wb(int* p, int* size, int x, int y) // quick union has a different logic from quick union
{
	    // Note that sixe array has also been maintained with respect to every element

	    int rootx, rooty;
			
		rootx = root_wb(p, x);// roots are calculated
		rooty = root_wb(p, y);// roots are calculated
		if (size[rootx] <= size[rooty]) // now the sizes are compared and if the destination is smaller then its label is changed else opposite
		{
			p[rootx] = p[rooty];
			size[rooty] += size[rootx]; // further the size is also increased
		}
		else
		{
			p[rooty] = p[rootx];
			size[rootx] += size[rooty];
		}
	

}

int main()
{
	int pair[N]; // pair array
	int count = 0;
	int size[N];// size array in quick union weighted

	for (int i = 0; i < N; i++) // initialisation of the pairs array and the size array
	{
		pair[i] = i;
		size[i] = 1;
	}

	fstream source;

	source.open("32pair.txt");

	if (!source)
	{
		cout << "File could not be opened" << endl;
		exit(1);
	}

	int element1, element2, temp;


	
	
	//quick union method with weight balancing for the solution same as all
	while (source >> temp)
	{
		element1 = temp;
		source >> element2;
		count++;

		if (!long_find_wb(pair, element1, element2))
		{
			quickunion_wb(pair, size, element1, element2);
			cout << element1 << "\t" << element2 << endl;
		}
		
	}

	

	cout << "The complexity of the quick find algorithm for " << count << " size data set is " << complexity_counter << endl;

	

}


