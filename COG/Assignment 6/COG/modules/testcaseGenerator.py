from .pythonSolutions import *
import numpy as np
import math




def generateFile(write_file_path, num_files):
    file_names = []

    for file_index in range(num_files):
        # Randomly generate number of records
        num_records = np.random.randint(5, 15)

        # Generate Names
        potential_names = ['Molly', 'Fred', 'Diana', 'Shelia', 'Ted', 'Anne', 'Tasha', 'Megan', 'Vernon', 'Richard', 'Nancy', 'Tara', 'Bernard', 'Roger', 'Michael', 'Charlotte', 'Ernesto', 'Joann', 'Sonya', 'Ronald', \
         'Lucia', 'Harry', 'Ivan', 'Freddie', 'Janie', 'Leonard', 'Merle', 'Duane', 'Robyn', 'Penny', 'Hugh', 'Mae', 'Louis', 'Garrett', 'Aaron', 'Shelly', 'Danielle', 'Felix', 'Clarence', 'Patty',  \
         'Phil', 'Wade', 'Misty', 'Alton', 'Shawn', 'Roderick', 'Bridget', 'Minnie', 'Emily', 'Jody', 'Edwin', 'Jan', 'Guadalupe', 'Erma', 'Lisa', 'Corey', 'Kayla', 'Ollie', 'Pauline', 'Sherman', 'Flora', \
         'Alan', 'Lois', 'Santos', 'Pearl', 'Darryl', 'Ruby', 'Ken', 'Gloria', 'Sean', 'Jean', 'Trevor', 'Ashley', 'Eduardo', 'Natalie', 'Arlene', 'Erik', 'Florence', 'Daisy', 'Bernice', 'Sheldon', 'Samantha', \
         'Lora', 'Shane', 'Darlene', 'Dewey', 'Roland', 'Julius', 'Dorothy', 'Carole', 'George', 'Jamie', 'Al', 'Rhonda', 'Gerald', 'Carrie', 'Hubert', 'Marcus', 'Cody', 'Johnnie']

        random_start_index = np.random.randint(0, len(potential_names)-num_records-1)

        names = potential_names[random_start_index:random_start_index+num_records]

        # Generate scores
        # generate number of scores


        # Create input file
        infile_name = "infile_{}.txt".format(file_index)
        file_index += 1
        file_names.append(infile_name)
        file_path = write_file_path + infile_name;
        with open(file_path, "w") as outfile:
            for index, name in enumerate(names):
                outfile.write(name)
                outfile.write(",")

                num_scores = np.random.randint(3, 8)
                for score_index in range(num_scores):
                    random_score = min(np.random.normal(82.5, 10), 99.5)
                    outfile.write("{:0.5f}".format(random_score))
                    if score_index == num_scores-1:
                        outfile.write("\n")
                    else:
                        outfile.write(",")

    return file_names





def array_to_string(array):
    array_string = "["

    for index, element in enumerate(array):
        new_element = str(element)
        new_element = new_element[:7]
        element = float(new_element)
        if index == len(array)-1:
            array_string += "{:0.1f}]".format(element)
        else:
            array_string += "{:0.1f}, ".format(element)

    return array_string


def Part1_CountLinesTest(test_input, print_input, test_output, write_file_path, files, output_file_paths, output_index):
    """
        Part 1
        ------------------------------------------------------------
         1 test case - 5 points
    """

    test_cases = 1
    test_input.append(str(test_cases))


    # Test cases
    for test_case_num in range(test_cases):
        # Pick a random input file and set its path
        random_file_name = files[np.random.randint(len(files))]
        random_file_path = write_file_path + random_file_name

        # Generate the output
        expected_output = "Number of lines: {}".format(countFileLines(random_file_path))

        # Append test input and output to arrays
        test_input.append(random_file_path)
        test_output.append(expected_output)
        print_input.append("File: {} (randomly generated)\n".format(random_file_name))


def Part2_ReadScoresTest(test_input, print_input, test_output, write_file_path, files, output_file_paths, output_index):
    """
        Part 2
        ------------------------------------------------------------
        3 test cases - 5 pts each
    """

    test_cases = 3
    test_input.append(str(test_cases))


    # Test cases
    for test_case_num in range(test_cases):

        # Pick a random input file and set its path
        random_file_name = files[np.random.randint(len(files))]
        random_file_path = write_file_path + random_file_name


        names, averages, number_of_records = readScores(random_file_path)
        expected_output1 = "Number of records: {}".format(number_of_records)
        expected_output2 = "Names array: {}".format(names)
        expected_output3 = "Average scores array: " + array_to_string(averages)


        # Set inputs
        test_input.append(str(countFileLines(random_file_path)))
        test_input.append(random_file_path)

        # Set print inputs (for printing inputs sent during test cases)
        print_input.append("File: {} (randomly generated)\n".format(random_file_name))

        # Set outputs
        test_output.append(expected_output1)
        test_output.append(expected_output2)
        test_output.append(expected_output3)



def Part3_WriteGradesTest(test_input, print_input, test_output, write_file_path, files, output_file_paths, output_index):
    """
        Part 3
        ------------------------------------------------------------
        3 cases - 10 pts each
    """

    test_cases = 3
    test_input.append(str(test_cases))


    # Random Pieces
    for test_case_num in range(test_cases):

        random_file_name = files[np.random.randint(len(files))]
        random_file_path = write_file_path + random_file_name

        expected_output_size = "Number of lines: {}".format(countFileLines(random_file_path))

        names, averages, records = readScores(random_file_path)

        outfile_name = "expected_out_{}.txt".format(output_index)
        outfile_path = write_file_path + outfile_name
        writeGrades(outfile_path, names, averages)


        student_outfile_name = "student_out_{}.txt".format(output_index)
        student_outfile_path = write_file_path + student_outfile_name

        output_index += 1

        test_input.append(str(countFileLines(random_file_path)))
        test_input.append(random_file_path)
        test_input.append(student_outfile_path)

        print_input.append("File: {} (randomly generated)\n".format(random_file_name))


        output_file_paths.append([outfile_path, student_outfile_path])



def generateTestData(test_case_num, write_file_path, files, output_index):
    """
        EDIT THIS FUNCTION PER ASSIGNMENT -- TEST CASES GO HERE
    """
    test_input = [str(test_case_num)]
    print_input = []
    test_output = []
    output_file_paths = []


    parts = [Part1_CountLinesTest, Part2_ReadScoresTest, Part3_WriteGradesTest]

    parts[test_case_num-1](test_input, print_input, test_output, write_file_path, files, output_file_paths, output_index)

    return test_input, print_input, test_output, output_file_paths
