from .pythonSolutions import *
import numpy as np
import math


def generatePart1(test_input, print_input, test_output):
    """
        Part 1
        ------------------------------------------------------------
        Test cases:
          3. RANDOM x3
        X POINTS EACH test case
    """
    test_cases = 3

    test_input.append(str(test_cases))

    # Random Pieces
    for test_case_num in range(test_cases):
        random_value = np.random.randint(1, 10)
        random_size = np.random.randint(4, 10)
        fill_array = fillArray(random_size, random_value)

        expected_output = "Filled array: {}".format(fill_array)

        test_input.append(str(random_size))
        test_input.append(str(random_value))

        print_input.append(str("\tSize: {} \n\tValue: {}\n".format(random_size, random_value)))
        test_output.append(expected_output)


def generatePart2(test_input, print_input, test_output):
    """
        Part 2
        ------------------------------------------------------------
        Test cases:
          3. RANDOM x3
        X POINTS EACH test case
    """
    test_cases = 3
    test_input.append(str(test_cases))
    # Random Pieces
    for test_case_num in range(test_cases):
        random_size = np.random.randint(4, 10)
        scores_array = [np.random.normal(80, 10) for _ in range(random_size)]

        grades_array = calculateGrades(scores_array)

        expected_output = "Grades array: {}".format(grades_array)

        test_input.append(str(random_size))

        test_print = []
        for score in scores_array:
            test_input.append(str(score))
            test_print.append(float("{:0.1f}".format(score)))

        print_input.append(str("\tScores Array: {} \n\tSize: {}\n".format(test_print, random_size)))
        test_output.append(expected_output)



def generatePart3(test_input, print_input, test_output):
    """
        Part 3
        ------------------------------------------------------------
        Test cases:
          3. RANDOM x3
        X POINTS EACH test case
    """
    test_cases = 3
    test_input.append(str(test_cases))
    # Random Pieces
    for test_case_num in range(test_cases):
        random_size = np.random.randint(4, 10)
        scores_array = [np.random.normal(80, 10) for _ in range(random_size)]

        average_score = getAverageScore(scores_array)

        expected_output = "Average score: {:0.1f}".format(average_score)

        test_input.append(str(random_size))

        test_print = []
        for score in scores_array:
            test_input.append(str(score))
            test_print.append(float("{:0.1f}".format(score)))

        print_input.append(str("\tScores Array: {} \n\tSize: {}\n".format(test_print, random_size)))
        test_output.append(expected_output)


def generatePart4(test_input, print_input, test_output):
    """
        Part 4
        ------------------------------------------------------------
        Test cases:
          3. RANDOM x3
        X POINTS EACH test case
    """
    test_cases = 3
    test_input.append(str(test_cases))
    # Random Pieces
    for test_case_num in range(test_cases):
        random_size = np.random.randint(4, 10)
        scores_array = [np.random.normal(80, 10) for _ in range(random_size)]

        min_score = getMinScore(scores_array)

        expected_output = "Min score: {:0.1f}".format(min_score)

        test_input.append(str(random_size))

        test_print = []
        for score in scores_array:
            test_input.append(str(score))
            test_print.append(float("{:0.1f}".format(score)))

        print_input.append(str("\tScores Array: {} \n\tSize: {}\n".format(test_print, random_size)))
        test_output.append(expected_output)


def generatePart5(test_input, print_input, test_output):
    """
        Part 5
        ------------------------------------------------------------
        Test cases:
          3. RANDOM x3
        X POINTS EACH test case
    """
    test_cases = 3
    test_input.append(str(test_cases))
    # Random Pieces
    for test_case_num in range(test_cases):
        random_size = np.random.randint(4, 10)
        scores_array = [np.random.normal(80, 10) for _ in range(random_size)]

        max_score = getMaxScore(scores_array)

        expected_output = "Max score: {:0.1f}".format(max_score)

        test_input.append(str(random_size))

        test_print = []
        for score in scores_array:
            test_input.append(str(score))
            test_print.append(float("{:0.1f}".format(score)))

        print_input.append(str("\tScores Array: {} \n\tSize: {}\n".format(test_print, random_size)))
        test_output.append(expected_output)


def generatePart6(test_input, print_input, test_output):
    """
        Part 6
        ------------------------------------------------------------
        Test cases:
          3. RANDOM x3
        X POINTS EACH test case
    """
    test_cases = 3
    test_input.append(str(test_cases))
    # Random Pieces
    for test_case_num in range(test_cases):
        random_size = np.random.randint(4, 10)
        unsorted_scores_array = [np.random.normal(80, 10) for _ in range(random_size)]

        sorted_scores_array = sortScores(unsorted_scores_array)


        test_input.append(str(random_size))


        for index, score in enumerate(sorted_scores_array):
            formatted_score = "{:0.1f}".format(score)
            sorted_scores_array[index] = float(formatted_score)
            test_input.append(formatted_score)

        expected_output = "Sorted array: {}".format(sorted_scores_array)



        # For printing
        test_print = []
        for score in unsorted_scores_array:
            test_print.append(float("{:0.1f}".format(score)))

        print_input.append(str("\tUnsorted Array: {} \n\tSize: {}\n".format(test_print, random_size)))
        test_output.append(expected_output)



def generatePart7(test_input, print_input, test_output):
    """
        Part 7
        ------------------------------------------------------------
        Test cases:
          3. RANDOM x3
        X POINTS EACH test case
    """
    test_cases = 3
    test_input.append(str(test_cases))
    # Random Pieces
    for test_case_num in range(test_cases):
        random_size = np.random.randint(4, 10)
        scores_array = [np.random.normal(80, 10) for _ in range(random_size)]




        for index, score in enumerate(scores_array):
            formatted_score = "{:0.1f}".format(score)
            scores_array[index] = float(formatted_score)


        median_score = getMedian(scores_array)

        expected_output1 = "Median score: {:0.2f}".format(median_score)
        expected_output2 = "Original scores array: {}".format(scores_array)
        test_input.append(str(random_size))

        test_print = []
        for score in scores_array:
            test_input.append(str(score))
            test_print.append(float("{:0.1f}".format(score)))

        print_input.append(str("\tScores Array: {} \n\tSize: {}\n".format(test_print, random_size)))
        test_output.append(expected_output1)
        test_output.append(expected_output2)




def generatePart8(test_input, print_input, test_output):
    """
        Part 8
        ------------------------------------------------------------
        Test cases:
          3. RANDOM x3
        X POINTS EACH test case
    """
    test_cases = 3
    test_input.append(str(test_cases))
    grades = ["A", "B", "C", "D", "F"]
    # Random Pieces
    for test_case_num in range(test_cases):
        random_size = np.random.randint(4, 10)
        scores_array = [np.random.normal(80, 10) for _ in range(random_size)]
        grades_array = calculateGrades(scores_array)

        random_grade = grades[np.random.randint(len(grades))]
        grade_count = countGrade(grades_array, random_grade)

        expected_output = "Grade count: {}".format(grade_count)

        test_input.append(str(random_size))
        test_input.append(str(random_grade))

        for grade in grades_array:
            test_input.append(str(grade))


        print_input.append(str("\tGrades Array: {} \n\tGrade: {} \n\tSize: {}\n".format(grades_array, random_grade, random_size)))
        test_output.append(expected_output)




def generateTestData(test_case_num):
    """
        EDIT THIS FUNCTION PER ASSIGNMENT -- TEST CASES GO HERE
    """
    test_input = [str(test_case_num)]
    print_input = []
    test_output = []

    parts = [generatePart1, generatePart2, generatePart3, generatePart4,\
             generatePart5, generatePart6, generatePart7, generatePart8]

    parts[test_case_num-1](test_input, print_input, test_output)

    return test_input, print_input, test_output
