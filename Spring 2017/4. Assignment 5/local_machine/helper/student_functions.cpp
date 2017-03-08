#include<iostream>
using namespace std;

/**************************************************************************
The fillArray() function will take in three arguments, an array of integers,
the size of the array and an integer value with which the array has to be initialized.
You should pass the reference of your integer array that you declare in your main function to this function.
The function should fill the entire array with the given value. The function does not return any value.
**************************************************************************/

void fillArray(int data[],int size, int value)
{
	for (int i = 0; i < size; i++) {
		data[i] = value;
	}
}

/**************************************************************************
This function will populate your grades array based on the scores stored in your scores array.
The grades should be calculated based on the following rules and stored into your grades array.
**************************************************************************/

void calculateGrades(float scores [],char grades[], int size) {

	for (int i = 0; i < size; i++) {
	    if (scores[i] >= 90) {
	        grades[i] = 'A';
	    } else if (scores[i]  >= 80) {
	        grades[i] = 'B';
	    } else if (scores[i]  >= 70) {
	        grades[i] = 'C';
	    } else if (scores[i]  >= 60) {
	        grades[i] = 'D';
	    } else {
	        grades[i] = 'F';
	    }
	}
}

/**************************************************************************
The getAverageScore() function will take two arguments, i.e. the  reference of your scores array
and  the size of the array(which is also the number of students). The function should return the
average score of the students which should be of float type.
**************************************************************************/

float getAverageScore (float scores[], int size) {
	float sum = 0.0;
	for (int i = 0; i < size; i++) {
		sum +=scores[i];
	}
	return sum/size;
}

/**************************************************************************
The getMinScore() function should take in two arguments, i.e. the reference of your scores array
and the size of the array. The function should return the minimum score of all the scores which should be of float type.
**************************************************************************/

float getMinScore(float scores[],int size) {
	float min = 9999;

	for (int i = 0; i < size; i++) {
		if ( min > scores[i]) {
			min = scores[i];
		}
	}

	return min;
}

/**************************************************************************
The getMaxScore() function should take two arguments, i.e. the reference of your scores array
and the size of the array. The function should return the maximum score of all the scores which should be of float type.
**************************************************************************/

float getMaxScore(float scores[],int size) {
	float max = -1;

	for (int i = 0; i < size; i++) {
		if ( max < scores[i]) {
			max = scores[i];
		}
	}

	return max;
}

/**************************************************************************
The sortScores() function will take two arguments, i.e. the reference of your scores array and the size of the array.
The function does not return any value.
**************************************************************************/

void sortScores(float scores[],int size) {
	float temp = 0;
	bool flag = true;

	while(flag) {
		flag = false;
		for (int i = 0;i<size-1;i++) {
			if (scores[i] > scores[i+1]) {
				temp = scores[i];
				scores[i] = scores[i+1];
				scores[i+1] = temp;
				flag = true;
			}
		}
	}
}

/**************************************************************************
The getMedian function should take two arguments, i.e. the reference of your scores array and the size of the array.
The function should return the median score of the students which should be of float type.
**************************************************************************/

float getMedian(float scores[],int size) {
	float temp[size] ;
	for (int i = 0;i<size;i++) {
		temp[i] =  scores[i];
	}
	sortScores(temp, size);
	int mid = size / 2;
	float median = 0;

	if (size % 2 == 0) {
		median = (temp[mid-1] + temp[mid])/2;
	} else {
		median = temp[mid];
	}

	return median;
}

/**************************************************************************
This function takes in three arguments, i.e. the reference of the grades array, the grade character whose occurrence you want to count
and the size of the array. The function should return the count of students who have secured this grade.
**************************************************************************/

int countGrade(char grades[],char grade, int size) {
	int count = 0;
	for (int i = 0;i<size;i++) {
		if (grades[i] == grade) {
			count++;
		}
	}
	return count;
}
