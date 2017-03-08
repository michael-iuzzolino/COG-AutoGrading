import numpy as np


def countFileLines(filename):
	counter = 0
	with open(filename, "r") as infile:
		for line in infile:
			counter += 1

	return counter


def readScores(filename):
	names = []
	average_scores = []

	record_counter = 0
	with open(filename, "r") as infile:
		for line in infile:
			line_array = line.split(",")
			names.append(line_array[0])
			average_score = np.average([float(x) for x in line_array[1:]])
			average_scores.append(average_score)

			record_counter += 1

	return names, average_scores, record_counter


def writeGrades(filename, names, average_scores):
	# Sort names and average scores

	# Sort names
	sorted_names = []
	for name in sorted(names):
		sorted_names.append(name)

	# Sort scores
	sorted_scores = []
	for sorted_name in sorted_names:
		index = names.index(sorted_name)
		sorted_scores.append(average_scores[index])


	with open(filename, "w") as outfile:
		for (name, average_score) in zip(sorted_names, sorted_scores):
			if average_score >= 90:
				grade = "A"
			elif average_score >= 80:
				grade = "B"
			elif average_score >= 70:
				grade = "C"
			elif average_score >= 60:
				grade = "D"
			else:
				grade = "F"

			outfile.write("{}, {}, {}\n".format(name, average_score, grade))
