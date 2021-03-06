#!/usr/bin/env python3

"""
Author: Michael Louis Iuzzolino
Institution: University of Colorado Boulder

CSCI 1300 - Assignment 3 - Spring 2017
"""

import os,sys,inspect
import math, time
import numpy as np
import textwrap
import subprocess
import re

from modules.testcaseGenerator import generateTestData
from modules.GradingUtilities import studentFeedback, compileCPPFile
from modules import SubmissionFinder


class GradeSubmission():

    def __init__(self, submission_directory, COG_script_directory, local_test=False):
        """
            Constructor
        """
        os.chdir(COG_script_directory)                                   # Changes current working directory to given path; returns None in all the cases

        self.local_system_test = local_test
        self.submission_directory_name = submission_directory      # Sets up
        self.deductions = []
        self.student_files_path = []
        self.student_file_names = []
        self.student_files_content = []
        self.initialize_assignment_specifics()

        self.run_main_grading_sequence()



    def initialize_assignment_specifics(self):
        """
            EDIT THIS FUNCTION PER ASSIGNMENT -- TEST CASES GO HERE
        """
        self.max_score = 100
        self.starting_grade = 100                                             # Set max grade

        # Set deductions
        self.missing_file_deduction = 90
        self.compile_fail_deduction = 100
        self.missing_function_deduction = 60
        self.incorrect_answer_deduction = 10
        self.no_answer_deduction = 100

        self.deduction_dict = {"1" : 4,
                               "2" : 5,
                               "3" : 12,
                               "4" : 8}



        # File names
        # self.expected_files = ["main.cpp", "Assignment4.cpp"]
        self.expected_files = ["Assignment4.cpp"]
        self.helper_files = ["Assignment4.cpp"]

        self.number_expected_files = len(self.expected_files)
        self.number_expected_helper_files = len(self.helper_files)

        # Function names
        self.function_names = ["calcSimilarity",
                               "listSequencePositions",
                               "compareDNA",
                               "compare3Genomes"]


        # Define the required functions in their full name (for printing later)
        self.required_functions = ["float calcSimilarity (string sequenceOne, string sequenceTwo)",
                                   "void listSequencePositions(string genomeSequence, string genomeName, string seq)",
                                   "float compareDNA(string genome, string seq)",
                                   "void compare3Genomes(string genome1, string name1,string genome2, string name2, string genome3, string name3, string seq)"]


        # Catch phrases for parsing student output
        self.catch_phrases = ["Similarity",
                              "Human match locations",
                              "Mouse match locations",
                              "Unknown match locations",
                              "Best match:",
                              "Test: "]


        # Generate test cases
        self.number_test_cases = len(self.function_names)
        self.__generate_test_cases()





    def __generate_test_cases(self):
        self.test_case_dict = {}


        # Generate test_data
        for test_case_num in range(1, self.number_test_cases+1):
            test_input, test_output = generateTestData(test_case_num)
            self.test_case_dict[test_case_num] = {"input" : test_input, "output" : test_output}




    """
                    You should not need to edit anything below this line
            --------====================================================--------
    """













    def run_main_grading_sequence(self):
        """
        Step 0.a: Locate student's submission
            IF all submissions found, go to step 1.
            ELSE, deduct 100 points and EXIT.
        """
        studentFeedback("\n" + "="*100)
        studentFeedback("Locating Submission...")
        found_submission = self.locate_submissions()

        if not found_submission:
            studentFeedback("\t\t\tCould not locate submission.")
            return
            # EXIT
        studentFeedback("\t\t\tSuccess!")



        # """
        # Step 1: Check that the student's code compiles
        #
        #     IF compile, go to step 2.
        #     ELSE: Deduct 100 points and EXIT.
        # """
        # studentFeedback("\n" + "="*100)
        # studentFeedback("Checking Compile...", new_line=False),
        # code_compiles = self.check_compile()
        #
        # if not code_compiles:
        #     self.make_deduction(self.compile_fail_deduction, "COG could not compile your file. Ensure the .cpp file compiles on your system.")
        #     studentFeedback("\tERROR! Does not compile!")
        #     return
        #     # EXIT
        #
        # studentFeedback("\tSuccess!")



        """
        Step 2: Create student_functions_file.cpp
        a. Change student's problem1.cpp main() to defunct()
        b. Copy each line of student's problem1.cpp into new file, student_functions_file.cpp, created at helper_folder_path
        """
        studentFeedback("\n" + "="*100)
        studentFeedback("Creating Alternate file...", new_line=False),
        self.move_helper_files()
        studentFeedback("\tSuccess!")



        """
        Step 3: Check that all required functions exist
            IF all required functions, go to step 3.
            ELSE: Deduct 1 / number_required_functions per missing function, then EXIT.
        """
        studentFeedback("\n" + "="*100)
        studentFeedback("Checking for Required Functions... "),
        found_all_functions = self.check_functions()
        if not found_all_functions:
            studentFeedback("\tERROR: Could not find all required functions. Ensure you are using void in function definitions as specified in assignment writeups.")
            return
            # EXIT
        studentFeedback("\tSuccess!")




        """
        Step 4: Compile helper.cpp
        IMPORTANT: Be sure to pass it input_name_1, input_name_2, output_name_1, and output_name_2 for argv
        """
        studentFeedback("\n" + "="*100)
        studentFeedback("Creating Helper.cpp file...", new_line=False),
        helper_compiled_name = self.helper_file_path.replace(".cpp", "")

        if (compileCPPFile(self.helper_file_path, helper_compiled_name)):
            studentFeedback("\tSuccess!")
        else:
            self.make_deduction(self.compile_fail_deduction, "COG could not compile your file. Ensure the .cpp file compiles on your system.")
            studentFeedback("\tERROR! Does not compile!")
            return



        """
        Step 5: Run test cases
        """
        studentFeedback("\n" + "="*100)
        studentFeedback("Running Test Cases...\n"),
        for test_case_num, test_case in self.test_case_dict.items():
            self.run_test_case(test_case_num, test_case, self.helper_file_path.replace(".cpp", ""))






    def locate_submissions(self):
        """
            Docstring Under Construction
            Find the submission in the folder - sometimes it isn't named exactly
        """
        found_some_files = False
        number_files_found = 0

        submission_finder = SubmissionFinder.SubmissionFinder()      # Creates submissionFinder object

        # Iterates through expected file names and checks if each are in the submissions directory

        for expected_file in self.expected_files:
            submission_file_name = submission_finder.findSubmission(self.submission_directory_name, expected_file.strip(".cpp").strip(".h"))

            # File found
            if submission_file_name:
                found_some_files = True
                number_files_found += 1

                studentFeedback("\t--   '{}' file successfully located!".format(submission_file_name))

                # Set location of files
                self.student_file_names.append(submission_file_name)
                submission_file_path = self.submission_directory_name + "/" + submission_file_name
                self.student_files_path.append(submission_file_path)

            # File not found
            else:
                studentFeedback("\t--   ** '{}' file not found. **".format(expected_file))
                self.make_deduction(self.missing_file_deduction, "Could not locate your {}.cpp file. Ensure your file is correctly named and zipped.".format(expected_file))

        studentFeedback("\n\t{} / {} files successfully located.".format(number_files_found, self.number_expected_files))
        return found_some_files



    def check_compile(self):

        # Iterate through submission files (if numerous .cpp in .zip file)
        for submission_file, assignment_name in zip(self.student_files_path, self.student_file_names):
            if assignment_name in self.helper_files:
                continue
            compiled_program_name = submission_file.replace(".cpp", "")
            program_compiles = compileCPPFile(submission_file, compiled_program_name)


            if not program_compiles:
                self.make_deduction(self.compile_fail_deduction, "{} does not compile. Check your coding with c++11 standard.".format(assignment_name))
                return False

        return True



    def write_helper(self):
        # Sets paths for LOCAL SYSTEM TESTS
        if self.local_system_test:
            self.helper_file_path = "helper/helper.cpp"
            self.student_helper_file_paths = ["helper/student_functions.cpp"]

        # Sets paths for use on COG server
        else:
            current_helper_path = os.getcwd() + "/COG/helper.cpp"

            submission_write_path = self.submission_directory_name + "/helper.cpp"
            submission_write_path = submission_write_path.replace("//", "/")
            with open(current_helper_path, "r") as infile, open(submission_write_path, "w") as outfile:
                for line in infile:
                    outfile.write(line)


            # Declare the helper file's path
            self.helper_file_path = submission_write_path

            # Declare the paths to the now defunct student files
            self.student_helper_file_paths = [self.submission_directory_name + "/student_functions.cpp"]



    def move_helper_files(self):
        # Setup helper file
        self.write_helper()

        index = 0
        for assignment_path, assignment_name in zip(self.student_files_path, self.student_file_names):
            if assignment_name not in self.helper_files:
                continue

            with open(assignment_path, "r") as student_file, open(self.student_helper_file_paths[index], "w") as student_helper_file:
                for line in student_file:
                    student_helper_file.write(line)

            # Open the student's file again, read all lines, and save to the student files content list
            with open(assignment_path, "r") as student_file:
                self.student_files_content.append(student_file.readlines())

            index += 1


        # Flatten the file content list
        flattened_file_content_list = [item.strip().lower() for file_i in self.student_files_content for item in file_i]
        self.student_files_content = flattened_file_content_list



    def check_functions(self):
        """Copies the student submission and changes their main method so that it can be compiled
        with a function checker program."""

        # Define required functions for checking in file and convert them to lower case
        check_required_functions = [self.split_function_string(func.lower()) for func in self.required_functions]


        number_of_required_functions = len(self.required_functions)   # Define number of required functions
        number_of_found_functions = 0                            # Define number of required functions found in the given file

        # Declare students script
        student_file_content = self.student_files_content
        # Flag functions as found
        found_all_functions = True

        # Iterate through each line in the students script
        for line in student_file_content:
            # Parse the line
            parsed_line = self.split_function_string(line)

            prev_len = len(check_required_functions)
            check_required_functions = self.match_function_string(parsed_line, check_required_functions)
            if prev_len > len(check_required_functions):
                number_of_found_functions += 1



        # Print student feedback to inform of number required functions found
        studentFeedback("\tFound {} / {} required functions".format(number_of_found_functions, number_of_required_functions))

        # Check if the required number of functions list is non zero - this means some were not found in student file
        if number_of_found_functions != number_of_required_functions:
            # Iterate through required functions that were not found
            for required_function in check_required_functions:
                # Iterate through the full function named list to find the correct one for printing to student in deductions
                for full_req_fnx in self.required_functions:
                    full_req_fnx_check = ' '.join(self.split_function_string(full_req_fnx.lower()))
                    if ' '.join(required_function) == full_req_fnx_check:
                        self.make_deduction(self.missing_function_deduction, "{:s} function is required, but is missing from or incorrectly defined in your program. Correct this function for full credit.".format(full_req_fnx))
                        found_all_functions = False

        return found_all_functions



    def split_function_string(self, function_string):
        #split on space , (, ), ',', and { then remove empty strings
        #but split on '//' first to remove comments
        parsed_function = re.split('\s|\(|\)|,|{', function_string)
        return [v for v in parsed_function if v != '']


    def match_function_string(self, user_func, expected_func_list):
        for required_func in expected_func_list:
            match = len(user_func) == len(required_func)                        #check that the function definitions have the same number of words

            for (observed_word, expected_word) in zip(user_func, required_func):
                observed_word = observed_word.replace("_", "")

                if (expected_word != '_') and (observed_word != expected_word):
                    match = False
                    break
            if match:
                expected_func_list.remove(required_func)
                return expected_func_list
        return expected_func_list





    def parse_student_answers(self, student_answers, test_number):
        # https://automatetheboringstuff.com/chapter7/

        new_answers = []
        for answers in student_answers:
            answer = answers.strip()

            for catch_phrase in self.catch_phrases:
                if catch_phrase.lower() in answer.lower():

                    if "similarity" in catch_phrase.lower():
                        temp_answer_list = answer.split(":")
                        number = temp_answer_list[1]
                        temp_answer_list[1] = "{:0.2f}".format(float(number))
                        answer = ": ".join(temp_answer_list)


                    if "339" in answer or "340" in answer:
                        answer = answer.strip("340")
                        answer = answer.strip("339")




                    new_answers.append(answer)

        if self.function_names[test_number-1] == "listSequencePositions":
            index_list = []
            for answer in new_answers:
                split_answer = answer.split(":")
                match_name = split_answer[0] + ": "
                match_indicies = split_answer[1].strip().split(" ")
                new_answer = [match_name, match_indicies]
                index_list.append(new_answer)

            new_answers = index_list

        return new_answers



    def run_test_case(self, test_case_num, test_case, helper_path):
        function_name = self.function_names[test_case_num-1]
        studentFeedback("Checking function: {}\n".format(function_name))

        total_points_lost = []

        input_feed = test_case["input"]
        expected_outputs = test_case["output"]

        if test_case_num == 4:
            studentFeedback("{:6s}{:8s}{}\n".format("", "Input Feed: ", input_feed[1:-1]))

        # Starts process
        process = subprocess.Popen(helper_path, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=sys.stderr, shell=True)

        # Sending inputs and receiving outputs and errs
        out, err = process.communicate(("\n".join(input_feed)).encode(), timeout=10) # Pass inputs and receive outputs and errs

        # Splits the console output by newline character into a list of all outputs
        student_answers = out.decode().split("\n")


        # Clean student answers from empty newlines at very end of program; e.g., very last cout has endl; this is fine!
        if student_answers[-1] == '':
            student_answers = student_answers[:-1]


        # Parse out student answers!
        student_answers = self.parse_student_answers(student_answers, test_case_num)


        # Check for correct answers
        num_student = len(student_answers)
        num_expected = len(expected_outputs)
        if num_student == 0:
            studentFeedback("\t***Function {} produces no output. Ensure you're following the writeup requirements.\n".format(function_name))
            total_points_lost.append([self.no_answer_deduction, "Your function {} has produced no outputs! Ensure you are following the exact requirements of the writeup.".format(function_name)])


        if self.function_names[test_case_num-1] == "listSequencePositions":

            counter = 0
            print_index = 0
            for expected_answer, student_answer in zip(expected_outputs, student_answers):
                try:
                    expected_name = expected_answer[0]
                    expected_indicies = expected_answer[1].strip().split(" ")

                    students_name = student_answer[0]
                    students_indicies = student_answer[1]
                except:
                    pass

                if counter % 3 == 0:
                    print("Input feed: {}".format(input_feed[print_index+1]))
                    print_index += 1



                total_required_indicies = len(expected_indicies)
                student_index_count = 0
                for student_index in students_indicies:
                    if student_index in expected_indicies:
                        student_index_count += 1
                        del expected_indicies[expected_indicies.index(student_index)]

                missing_number = max(0, total_required_indicies - student_index_count)
                total_deduction = self.deduction_dict[str(test_case_num)] * missing_number

                if missing_number > 0:
                    total_points_lost.append([total_deduction, "Incorrect Answer. Expected Output: {:30s}, Your Output: {:30s}".format(expected_answer_print, student_answer_print)])


                # Student answer string
                student_answer_print = ""
                student_answer_print += student_answer[0]
                for index in student_answer[1]:
                    student_answer_print += " {} ".format(index)

                # Expected answer string
                expected_answer_print = ""
                expected_answer_print += expected_answer[0]
                expected_answer_print += expected_answer[1]

                studentFeedback("{:6s}{:50s}{:10s}{:50s}".format("", "Expected Output", "", "Your Ouput"))
                studentFeedback("{:6s}{:50s}{:10s}{:70s}".format("", "---------------", "", "----------"))
                studentFeedback("{:6s}{:50s}{:10s}{:50s}{:2s}".format("", expected_answer_print, "", student_answer_print, ""))
                studentFeedback("\n\n")

                counter += 1

        else:
            counter = 0
            print_index = 1

            for expected_answer, student_answer in zip(expected_outputs, student_answers):
                if test_case_num == 1:
                    studentFeedback("{:6s}{:8s}{}".format("", "Input Sequence 1: ", input_feed[print_index]))
                    studentFeedback("{:6s}{:8s}{}".format("", "Input Sequence 2: ", input_feed[print_index+1]))
                    print_index += 2

                elif test_case_num == 3:
                    studentFeedback("{:6s}{:8s}{}".format("", "Input Sequence: ", input_feed[2*counter+1]))



                expected = expected_answer.replace(" ", "").lower()
                student = student_answer.replace(" ", "").lower()

                studentFeedback("{:6s}{:50s}{:10s}{:50s}".format("", "Expected Output", "", "Your Ouput"))
                studentFeedback("{:6s}{:50s}{:10s}{:70s}".format("", "---------------", "", "----------"))
                if expected != student:
                    studentFeedback("{:4s}{:2s}{:50s}{:10s}{:50s}{:2s}".format("", "**", expected_answer, "", student_answer, "**"))
                    points_lost = self.deduction_dict[str(test_case_num)]
                    total_points_lost.append([points_lost, "Incorrect Answer. Expected Output: {:30s}, Your Output: {:30s}".format(expected_answer, student_answer)])
                else:
                    studentFeedback("{:6s}{:50s}{:10s}{:50s}{:2s}".format("", expected_answer, "", student_answer, ""))
                studentFeedback("\n\n")

                counter += 1
        for point_lost in total_points_lost:
            self.make_deduction(point_lost[0], point_lost[1])





    def make_deduction(self, points_lost, message):
        """
        Appends new deduction to deductions list; indicates points lost and a message pertaining to the lost points
        """
        self.deductions.append((-points_lost, message))


    def grade_and_comment(self):
        """
            Loops through the deductions list and calculates total lost points as well as collecting the grading comments.
            Assigns grade and reports comments to student.
        """

        comments = ""                                           # Initialize comments string

        # Iterate through deductions list and decrement grade and append respective comment to comments string.
        for gradeDeduction, comment in self.deductions:
            self.starting_grade += gradeDeduction
            comments += ("[%.1f] " % gradeDeduction) + comment + "\n"

        # Case: Student has 100%
        if (len(self.deductions)==0):
            comments = "Great work!"

        # Case: Less than 100%. Prints comments to student for suggestions on improvement.
        else:
            comments = comments.strip("\r").strip("\n")

        self.comments = comments            # Stores comments to object
        self.final_grade = max(round(self.starting_grade),0)    # Stores grade to object


    def give_feedback(self):
        """
            Sends comments to studentFeedback object for report.
        """
        studentFeedback(self.comments)



    def print_grade(self):
        """
            Prints the final grade to stdout
        """
        print(max(self.final_grade, 0))

        sys.stderr.write("__________________________\n")
        sys.stderr.write("Score ---------------> {:0.2f}/{:0.2f}\n".format(max(0, self.final_grade), self.max_score))




def main(argv):
    """
        MAIN function.
    """

    #Assign all output to the stderr stream as a catch all
    stdoutStream = sys.stdout
    sys.stdout = sys.stderr

    student_submission_directory = os.path.abspath(argv[0])
    COG_script_directory = os.path.abspath(argv[1])

    if not os.path.exists(student_submission_directory):
        sys.stderr.write("Could not find submission directory: '{:s}'\n".format(student_submission_directory))
        #return -1

    if not os.path.exists(COG_script_directory):
        sys.stderr.write("Could not find test directory: '{:s}'\n".format(COG_script_directory))


    submission = GradeSubmission(student_submission_directory, COG_script_directory)                 # Instantiate and construct grading object
    submission.grade_and_comment()                                 # Grade and generate comments for the assignment
    submission.give_feedback()                                     # Provide student feedback
    sys.stdout = stdoutStream
    submission.print_grade()                                       # Provide student final grade




if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
