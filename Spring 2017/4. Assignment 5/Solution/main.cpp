#include <iostream>
#include <cstdlib>
#include "Assignment5.cpp"
using namespace std;

template<typename T>
void printArray(T array[], int size) {
	for (int i =0; i< size; i++) {
		cout << array[i] << "  ";
	}
	cout << endl;
}

void fillScoreArray(float array[], int size) {
	for (int i=0;i< size; i++) {
		array[i] = rand()%100+1;
	}
}

int main() {

	int size = 15;
	int value = rand() % 100 +1;
	int array[size];
	char grade[size];
	float score[size];

	//part1
	cout << endl << "******************************************************************************" << endl;
	cout << "Array filled with value " << value <<": "<< endl;

	fillArray(array, size, value);
	printArray(array, size);

	//part2
	cout << endl << "******************************************************************************" << endl;
	fillScoreArray(score, size);
	calculateGrades(score, grade, size);

	cout << "Score Array: ";
	printArray(score, size);
	cout << "Grade Array: " ;
	printArray(grade, size);

	//part 3
	cout << endl << endl;
	cout << "The average Score is: " << getAverageScore(score, size) << endl;

	//part 4
	cout << endl << endl;
	cout << "The minimum Score is: " << getMinScore(score, size) << endl;

	//part 5
	cout << endl << endl;
	cout << "The maximum Score is: " << getMaxScore(score, size)<< endl;

	//part 6
	sortScores(score, size);
	cout << endl << endl;
	cout << "Sorted Array: ";
	printArray(score, size);

	//part 7
	cout << endl << endl;
	cout << "The median value is: " << getMedian(score, size) << endl;

	//part 8
	cout << endl << endl;
	cout << "The number of students with grade B are: " << countGrade(grade, 'B', size) << endl <<endl;

	return 0;
}
