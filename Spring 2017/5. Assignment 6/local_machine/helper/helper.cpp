#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <math.h>
#include <sstream>
#include <string>

#include "student_functions.cpp"


using namespace std;

int precision = 1;

template<typename T>
void printStringArray(T array[], int size)
{
	cout << "[";
	for (int i=0; i < size; i++)
	{
		if (i == size-1)
		{
			cout << "'" << array[i] << "'";
		}
		else
		{
			cout << "'" << array[i] << "', ";
		}
	}
	cout << "]" << endl;
}

template<typename T>
void printNumericArray(T array[], int size)
{
	cout << "[";
	for (int i=0; i < size; i++)
	{
		if (i == size-1)
		{
			cout << fixed << setprecision(precision) << array[i];
		}
		else
		{
			cout << fixed << setprecision(precision) << array[i] << ", ";
		}
	}
	cout << "]" << endl;
}


void Part1_CountLinesTest(int number_test_cases)
{
	int number_lines;
	string file_name;
	for (int i=0; i < number_test_cases; i++)
	{
		cin >> file_name;
		number_lines = CountLines(file_name);
		cout << "Number of lines: " << number_lines << endl;
	}
}


void Part2_ReadScoresTest(int number_test_cases)
{
	int array_size, number_records;
	string file_name;
	for (int i=0; i < number_test_cases; i++)
	{
		cin >> array_size;
		cin >> file_name;

		string *names = new string[array_size];
		float avg_scores[array_size];

		number_records = ReadScores(file_name, names, avg_scores, array_size);

		cout << "Number of records: " << number_records << endl;

		cout << "Names array: ";
		printStringArray(names, array_size);

		cout << "Average scores array: ";
		printNumericArray(avg_scores, array_size);

	}
}


void Part3_WriteGradesTest(int number_test_cases)
{
	int array_size, n_students, number_records;
	string infile_name, outfile_name;
	for (int i=0; i < number_test_cases; i++)
	{
		cin >> array_size;
		cin >> infile_name;
		cin >> outfile_name;
		string *names = new string[array_size];
		float avg_scores[array_size];

		number_records = ReadScores(infile_name, names, avg_scores, array_size);

		string filename = "infile.txt";
		WriteGrades(outfile_name, names, avg_scores, array_size);

	}
}




int main()
{
	string test_case_id;
	int number_test_cases;

	cin >> test_case_id;
	cin >> number_test_cases;

	if (test_case_id == "1")
	{
		Part1_CountLinesTest(number_test_cases);
	}
	else if (test_case_id == "2")
	{
		Part2_ReadScoresTest(number_test_cases);
	}
	else if (test_case_id == "3")
	{
		Part3_WriteGradesTest(number_test_cases);
	}

	return 0;
}
