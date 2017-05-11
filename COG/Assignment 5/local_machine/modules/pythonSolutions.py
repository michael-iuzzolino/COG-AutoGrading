import numpy as np


def fillArray(size, value):
	fill_array = [value for _ in range(size)]
	return fill_array


def calculateGrades(scores_array):
	grades_array = []
	for score in scores_array:
		if score >= 90:
			grades_array.append("A")
		elif score >= 80:
			grades_array.append("B")
		elif score >= 70:
			grades_array.append("C")
		elif score >= 60:
			grades_array.append("D")
		else:
			grades_array.append("F")

	return grades_array


def getAverageScore(scores_array):
	total = 0.0
	for score in scores_array:
		total += score

	return total / len(scores_array)


def getMinScore(scores_array):
	return min(scores_array)

def getMaxScore(scores_array):
	return max(scores_array)

def sortScores(unsorted_scores_array):
	sorted_scores = np.sort(unsorted_scores_array)

	sorted_array = [float("{:0.2f}".format(score)) for score in sorted_scores]


	return sorted_array



def getMedian(scores_array):
	return np.median(scores_array)

def countGrade(grades_array, grade):
	return grades_array.count(grade)
