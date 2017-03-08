#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <math.h>
#include "student_functions.cpp"
using namespace std;

int precision = 1;

template<typename T>
void printArray(T array[], int size)
{
	cout << "[";
	for (int i=0; i < size; i++)
	{
		if (i == size-1)
		{
			cout << array[i];
		}
		else
		{
			cout << array[i] << ", ";
		}
	}
	cout << "]";
}

template<typename T>
void printGradeArray(T array[], int size)
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




void part1(int number_test_cases)
{
	int size;
	int value;

	for (int i=0; i < number_test_cases; i++)
	{
		cin >> size;
		cin >> value;

		int array[size];

		cout << "Filled array: ";
		fillArray(array, size, value);
		printNumericArray(array, size);
	}
}


void part2(int number_test_cases)
{
	int size;
	for (int i=0; i < number_test_cases; i++)
	{
		cin >> size;
		float score[size];

		for (int i=0; i < size; i++)
		{
			cin >> score[i];
		}

		char grade[size];

		cout << "Grades array: ";
		calculateGrades(score, grade, size);
		printGradeArray(grade, size);
	}
}

void part3(int number_test_cases)
{
	int size;
	for (int i=0; i < number_test_cases; i++)
	{
		cin >> size;

		float score[size];

		for (int i=0; i < size; i++)
		{
			cin >> score[i];
		}

		cout << "Average score: " << fixed << setprecision(precision) << getAverageScore(score, size) << endl;
	}
}

void part4(int number_test_cases)
{
	int size;
	for (int i=0; i < number_test_cases; i++)
	{
		cin >> size;
		float score[size];

		for (int i=0; i < size; i++)
		{
			cin >> score[i];
		}

		cout << "Min score: " << fixed << setprecision(precision) << getMinScore(score, size) << endl;
	}
}

void part5(int number_test_cases)
{
	int size;
	for (int i=0; i < number_test_cases; i++)
	{

		cin >> size;
		float score[size];

		for (int i=0; i < size; i++)
		{
			cin >> score[i];
		}
		cout << "Max score: " << fixed << setprecision(precision) << getMaxScore(score, size)<< endl;
	}
}

void part6(int number_test_cases)
{
	int size;
	for (int i=0; i < number_test_cases; i++)
	{
		cin >> size;
		float score[size];
		for (int i=0; i < size; i++)
		{
			cin >> score[i];
		}

		sortScores(score, size);
		cout << "Sorted array: ";
		printNumericArray(score, size);
	}
}

void part7(int number_test_cases)
{
	int size;
	for (int i=0; i < number_test_cases; i++)
	{
		cin >> size;
		float score[size];

		for (int i=0; i < size; i++)
		{
			cin >> score[i];
		}
		cout << "Median score: " << fixed << setprecision(precision+1) << getMedian(score, size) << endl;
		cout << "Original scores array: ";
		printNumericArray(score, size);
	}
}

void part8(int number_test_cases)
{
	int size;
	char letter_grade;

	for (int i=0; i < number_test_cases; i++)
	{
		cin >> size;
		cin >> letter_grade;

		char grade[size];

		for (int i=0; i < size; i++)
		{
			cin >> grade[i];
		}

		cout << "Grade count: " << countGrade(grade, letter_grade, size) << endl;
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
		part1(number_test_cases);
	}
	else if (test_case_id == "2")
	{
		part2(number_test_cases);
	}
	else if (test_case_id == "3")
	{
		part3(number_test_cases);
	}
	else if (test_case_id == "4")
	{
		part4(number_test_cases);
	}
	else if (test_case_id == "5")
	{
		part5(number_test_cases);
	}
	else if (test_case_id == "6")
	{
		part6(number_test_cases);
	}
	else if (test_case_id == "7")
	{
		part7(number_test_cases);
	}
	else if (test_case_id == "8")
	{
		part8(number_test_cases);
	}

	return 0;
}
