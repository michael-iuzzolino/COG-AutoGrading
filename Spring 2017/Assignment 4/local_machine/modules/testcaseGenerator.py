from .pythonSolutions import *
import numpy as np


GENOMES = ["human", "mouse", "unknown"]


def generatePart1(test_input, test_output):
    """
        Part 1
        ------------------------------------------------------------
        Test cases:
          1. All match
          2. No match
          3. RANDOM x3
        4 POINTS EACH test case
    """
    # All Match
    seq1_input = generate_random_sequence(4, 10)
    seq2_input = seq1_input
    expected_output = "Similarity: {:0.2f}".format(problem1(seq1_input, seq2_input))

    test_input.append(seq1_input)
    test_input.append(seq2_input)
    test_output.append(expected_output)

    # No match  // Translate function (something like this)
    seq1_input = generate_random_sequence(4, 10)
    seq2_input = ""
    for char in seq1_input:
        if char == "A":
            seq2_input += "T"
        elif char == "T":
            seq2_input += "A"
        elif char == "G":
            seq2_input += "C"
        elif char == "C":
            seq2_input += "G"

    expected_output = "Similarity: {:0.2f}".format(problem1(seq1_input, seq2_input))

    test_input.append(seq1_input)
    test_input.append(seq2_input)
    test_output.append(expected_output)


    # Random Pieces
    for test_case_num in range(3):
        seq1_input, seq2_input = generate_random_sequences(4, 10)
        expected_output = "Similarity: {:0.2f}".format(problem1(seq1_input, seq2_input))

        test_input.append(seq1_input)
        test_input.append(seq2_input)
        test_output.append(expected_output)

    # Ends part 1
    test_input.append("*")



def generatePart2(test_input, test_output):
    """
        Part 2
        ------------------------------------------------------------
        Make it partial credit for catching partial number of matches,
        Test Cases:
        No Match - 1
        Multiple  - 3 random
        5 POINTS EACH
    """

    # No match
    seq_input = generate_random_sequence(10, 20)

    test_input.append(seq_input)
    for genome_name in GENOMES:
        result = problem2(genome_name, seq_input)
        expected_output = ["{} match locations: ".format(genome_name.capitalize()), result.strip()]
        test_output.append(expected_output)



    # Random
    for test_case_num in range(3):

        no_results_empty = False

        while not no_results_empty:
            results = []
            no_results_empty = True

            seq_input = generate_random_sequence(4, 6)

            for genome_name in GENOMES:
                results.append(problem2(genome_name, seq_input))

            for result in results:
                if (len(result.strip()) == 0) or (len(result.strip()) > 70):
                    no_results_empty = False


        test_input.append(seq_input)

        for genome_name, result in zip(GENOMES, results):
            expected_output = ["{} match locations: ".format(genome_name.capitalize()), result.strip()]
            test_output.append(expected_output)


    # Ends part 2
    test_input.append("*")


def generatePart2_5(test_input, test_output):
    """
        Part 2.5
        ------------------------------------------------------------
        3 test cases
        12 pts each
    """


    for test_case_num in range(3):
        seq_input = generate_random_sequence(5, 15)
        genome_input = GENOMES[np.random.randint(len(GENOMES))]
        genome = DNA_dict[genome_input]
        expected_output_1 = problem3_helper(genome, seq_input)

        test_input.append(seq_input)
        test_input.append(genome_input)
        test_output.append("Test: {:0.2f}".format(expected_output_1))

    # Ends part 2.5
    test_input.append("*")


def generatePart3(test_input, test_output):
    """
        Part 3
        ------------------------------------------------------------
        Part 4 24%
        3 test cases
        8 pts each
    """
    for test_case_num in range(3):
        seq_input = generate_random_sequence(5, 15)
        expected_outputs = problem3(seq_input)

        test_input.append(seq_input)
        for expected_output in expected_outputs:
            test_output.append("Best match: {}".format(expected_output))


    # Ends part 3
    test_input.append("*")



def generateTestData(test_case_num):
    """
        EDIT THIS FUNCTION PER ASSIGNMENT -- TEST CASES GO HERE
    """
    test_input = [str(test_case_num)]
    test_output = []

    parts = [generatePart1, generatePart2, generatePart2_5, generatePart3]
    parts[test_case_num-1](test_input, test_output)


    return test_input, test_output
