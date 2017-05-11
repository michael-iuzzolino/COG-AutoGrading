#!/usr/bin/env python3

"""
Author: Michael Louis Iuzzolino
Institution: University of Colorado Boulder

CSCI 1300 - Assignment 5 - Spring 2017
"""

import os,sys,inspect
import math, time
import numpy as np
import textwrap
import subprocess
import re

from modules.testcaseGenerator import generateTestData, generateFile
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
        self.max_score = 50
        self.starting_grade = 50                                             # Set max grade





        # File names
        # self.expected_files = ["main.cpp", "Assignment4.cpp"]
        self.expected_files = ["Assignment6.cpp"]
        self.helper_files = ["Assignment6.cpp"]
        self.exact_file_name = True;

        self.number_expected_files = len(self.expected_files)
        self.number_expected_helper_files = len(self.helper_files)


        # Setup read-write location
        if self.local_system_test:
            self.write_file_path = "files/"
        else:
            # self.write_file_path = os.getcwd() + "/COG/"
            self.write_file_path = self.submission_directory_name + "/"


        # Function names
        self.function_names = ["CountLines",
                               "ReadScores",
                               "WriteGrades"]


        # Define the required functions in their full name (for printing later)
        self.required_functions = ["int CountLines(string filename)",
                                   "int ReadScores(string filename, string names[], float avg_scores[], int array_size)",
                                   "void WriteGrades(string filename, string names[], float avg_scores[], int n_students)"]


        # Catch phrases for parsing student output
        self.catch_phrases = ["Number of lines:",
                              "Number of records:",
                              "Names array:",
                              "Average scores array:",
                              "output file."]

        # Generate test files
        number_input_files = 4
        self.input_files = generateFile(self.write_file_path, number_input_files)

        # Generate test cases
        self.number_function_tests = len(self.function_names)
        self.__generate_test_cases()



        # Set deductions
        self.missing_file_deduction = self.max_score
        self.compile_fail_deduction = self.max_score
        self.missing_function_deduction = self.max_score / len(self.required_functions) * 2.2
        self.no_answer_deduction = self.max_score

        self.deduction_dict = {"1" : 5,     # 1 test case, 5 pts each
                               "2" : 5,      # 3 test cases, 5 pts each
                               "3" : 10}     # 3 test cases, 10 pts each


    def __generate_test_cases(self):
        self.test_case_dict = {}
        self.input_print_dictionary = {}


        # Generate test_data
        output_index = 0
        for test_case_num in range(1, self.number_function_tests+1):
            test_input, print_input, test_output, self.output_file_paths = generateTestData(test_case_num, self.write_file_path, self.input_files, output_index)
            self.test_case_dict[test_case_num] = {"input" : test_input, "output" : test_output}
            self.input_print_dictionary[test_case_num] = {"input" : print_input}


    def parse_student_answers(self, student_answers, test_number):
        # https://automatetheboringstuff.com/chapter7/

        new_answers = []
        for answers in student_answers:
            answer = answers.strip()
            for catch_phrase in self.catch_phrases:
                if catch_phrase.lower() in answer.lower():
                    new_answers.append(answer)

        return new_answers



    def run_test_case(self, function_num, test_case, helper_path):
        function_name = self.function_names[function_num-1]
        studentFeedback("Checking function: {}".format(function_name))
        studentFeedback("==================={}\n".format("="*len(function_name)))

        total_points_lost = []

        input_feed = test_case["input"]
        expected_outputs = test_case["output"]

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
        student_answers = self.parse_student_answers(student_answers, function_num)


        # Check for correct answers
        num_student = len(student_answers)
        num_expected = len(expected_outputs)
        if num_student == 0 and function_name != "WriteGrades":
            studentFeedback("\t** ERROR: No output found.\n\n")
            loss_factor = 3 if (function_name == "ReadScores" or function_name == "WriteGrades") else 1
            points_lost = self.deduction_dict[str(function_num)] * loss_factor
            total_points_lost.append([points_lost, "{} produces no outputs matching the writeup! Ensure you are following the exact requirements of the writeup.".format(function_name)])

            # DEDUCT POINTS
            for point_lost in total_points_lost:
                self.make_deduction(point_lost[0], point_lost[1])

            return

        counter = 0
        print_index = 1
        input_print = self.input_print_dictionary[function_num]['input']

        if (function_name == "ReadScores"):

            test_case_number = 0
            for index, (expected_answer, student_answer) in enumerate(zip(expected_outputs, student_answers)):
                if index % 3 == 0:
                    test_case_number += 1

                    # PRINT TEST CASE NUMBER
                    studentFeedback("{:6s}{:8s}{}{:50s}".format("", "Testcase: ", test_case_number, ""))

                    # PRINT TEST CASE INPUT
                    studentFeedback("{:6s}{:70s}{:10s}{:50s}".format("", "Input", "", ""))
                    studentFeedback("{:6s}{:70s}{:10s}{:50s}".format("", "-----", "", ""))
                    studentFeedback("{:6s}{:70s}{:10s}{:50s}".format("", input_print[test_case_number-1], "", ""))

                    # PRINT TEST CASE OUTPUTS (expected vs. observed)
                    studentFeedback("{:6s}{:70s}{:20s}{:50s}".format("", "Expected Output", "", "Your Ouput"))
                    studentFeedback("{:6s}{:70s}{:20s}{:70s}".format("", "---------------", "", "----------"))

                # Format expected and student
                expected = expected_answer.replace(" ", "").lower()
                student = student_answer.replace(" ", "").lower()

                # Correct
                if expected == student:
                    if (index%3 == 1):
                        expected_re_match = re.split("\[|\]", expected_answer)
                        student_re_match = re.split("\[|\]", student_answer)

                        for zip_index, (expect, student) in enumerate(zip(expected_re_match, student_re_match)):
                            if (zip_index == 1):
                                for e_name, s_name in zip(expect.split(" "), student.split(" ")):
                                    studentFeedback("{:8s}{:70s}{:20s}{:70s}{:2s}".format("", e_name.strip(",'"), "", s_name.strip(",'"), ""))
                            else:
                                studentFeedback("\n{:6s}{:70s}{:20s}{:70s}{:2s}".format("", expect.replace(":", ""), "", student.replace(":", ""), ""))
                                studentFeedback("{:6s}{:70s}{:20s}{:70s}{:2s}".format("", "-"*len(expect.replace(":", "")), "", "-"*len(student.replace(":", "")), ""))

                    else:
                        studentFeedback("{:6s}{:70s}{:20s}{:70s}{:2s}".format("", expected_answer, "", student_answer, ""))

                # Incorrect
                else:
                    # Determine points lost
                    num_points_lost = self.deduction_dict[str(function_num)]

                    # Print
                    studentFeedback("{:4s}{:2s}{:70s}{:20s}{:70s}{:2s}".format("", "**", expected_answer, "", student_answer, "**"))
                    total_points_lost.append([num_points_lost, "Incorrect answer for function {}, Test case # {}. Expected Output: {:20s} - Your Output: {:30s}".format(function_name, test_case_number+1, expected_answer, student_answer)])

                if index % 3 == 2:
                    studentFeedback("\n")

                counter += 1

            studentFeedback("\n\n")


        elif function_name == "WriteGrades":


            studentFeedback("Note: If you see expected average = 85.30199999999999 and your output is 85.302, this is acceptable. \n \
            Do not try to force your output to have the same number of decimal points. \n \
            Average scores are accepted if the difference is below a threshold, as follows:  |expected - observed| < 0.001 \n \
            For example, |85.30199999999999 - 85.302| = 1.42e-14, which is well below a 0.001 difference. Therefore, your answer is accepted.\n \
            \n")
            self.compareOutputFiles(function_num, total_points_lost, function_name)


        else:



            for test_case_number, (expected_answer, student_answer) in enumerate(zip(expected_outputs, student_answers)):

                # PRINT TEST CASE INPUT
                studentFeedback("{:6s}{:70s}{:10s}{:50s}".format("", "Input", "", ""))
                studentFeedback("{:6s}{:70s}{:10s}{:50s}".format("", "-----", "", ""))
                studentFeedback("{:6s}{:70s}{:10s}{:50s}".format("", input_print[test_case_number], "", ""))


                # PRINT TEST CASE OUTPUTS (expected vs. observed)
                studentFeedback("{:6s}{:70s}{:10s}{:50s}".format("", "Expected Output", "", "Your Ouput"))
                studentFeedback("{:6s}{:70s}{:10s}{:70s}".format("", "---------------", "", "----------"))

                expected = expected_answer.replace(" ", "").lower()
                student = student_answer.replace(" ", "").lower()

                # Correct
                if expected == student:
                    studentFeedback("{:6s}{:70s}{:10s}{:70s}{:2s}".format("", expected_answer, "", student_answer, ""))

                # Incorrect
                else:
                    studentFeedback("{:4s}{:2s}{:70s}{:10s}{:70s}{:2s}".format("", "**", expected_answer, "", student_answer, "**"))
                    num_points_lost = self.deduction_dict[str(function_num)]

                    total_points_lost.append([num_points_lost, "Incorrect answer for function {}, Test case # {}. Expected Output: {:20s} - Your Output: {:30s}".format(function_name, test_case_number+1, expected_answer, student_answer)])

                studentFeedback("\n\n")

                counter += 1


        # DEDUCT POINTS
        for point_lost in total_points_lost:
            self.make_deduction(point_lost[0], point_lost[1])


    def compareOutputFiles(self, function_num, total_points_lost, function_name):

        number_correct = len(self.output_file_paths)

        for test_case, out in enumerate(self.output_file_paths):
            expected_output_path = out[0]
            student_output_path = out[1]


            # Ensure file can open:
            try:
                with open(expected_output_path, "r") as expected_file, open(student_output_path, "r") as student_file:
                    studentFeedback("\n\tSuccess opening file!\n")

            except FileNotFoundError:
                studentFeedback("{:2s}{:10s}{:40s}{:10s}{:40s}".format("", "** ERROR:", "Testcase {}: Your file produces no output file!".format(test_case+1), "", ""))
                total_points_lost.append([self.deduction_dict[str(function_num)], "ERROR: Testcase {}: Your function produces no output file.".format(test_case+1, function_name)])
                continue;




            studentFeedback("Testcase {}".format(test_case))
            studentFeedback("----------")


            # Check that student has successfully created output file
            # Get expected number of lines

            student_line_count = 0
            with open(student_output_path, "r") as student_file:
                for line in student_file:
                    student_line_count += 1

            if student_line_count == 0:
                studentFeedback("{:2s}{:10s}{:40s}{:10s}{:40s}".format("", "** ERROR:", "Testcase {}: Your file produces no output file!".format(test_case+1), "", ""))
                total_points_lost.append([self.deduction_dict[str(function_num)], "ERROR: Testcase {}: Your function produces no output file.".format(test_case+1, function_name)])
                continue

            incorrect = False
            with open(expected_output_path, "r") as expected_file, open(student_output_path, "r") as student_file:
                studentFeedback("{:2s}{:10s}{:40s}{:10s}{:40s}".format("", "", "Expected Outfile Line", "", "Student Outfile Line", ""))
                studentFeedback("{:2s}{:10s}{:40s}{:10s}{:40s}".format("", "", "---------------------", "", "--------------------", ""))
                for line_number, (expected_line, student_line) in enumerate(zip(expected_file, student_file), 1):

                    studentFeedback("{:2s}{:10s}{:40s}{:10s}{:40s}".format("", "Line {}:".format(line_number), expected_line.strip(), "", student_line))

                    # Expected output
                    expected_array = expected_line.strip().split(",")
                    expected_name = expected_array[0].strip()
                    expected_average = float(expected_array[1])
                    expected_grade = expected_array[2].strip()

                    # Student output
                    try:
                        student_array = student_line.split(",")
                        student_name = student_array[0].strip()
                        student_average = float(student_array[1])
                        student_grade = student_array[2].strip()
                    except IndexError:
                        studentFeedback("{:2s}{:10s}{:40s}{:10s}{:40s}".format("", "** ERROR:", "Testcase {}: Your file is not comma separated!".format(test_case+1), "", ""))
                        total_points_lost.append([self.deduction_dict[str(function_num)], "ERROR: Testcase {}: Your file is not comma separatedsh .".format(test_case+1, function_name)])
                        continue



                    if expected_name != student_name:
                        studentFeedback("{:2s}{:10s}{:40s}{:10s}{:40s}".format("**", "", "Expected name: {}".format(expected_name), "", "Student name: {}".format(student_name)))
                        incorrect = True

                    if np.abs(expected_average - student_average) > 0.001:
                        studentFeedback("{:2s}{:10s}{:40s}{:10s}{:40s}".format("**", "", "Expected average: {}".format(expected_average), "", "Student average: {}".format(student_average)))

                        incorrect = True

                    if expected_grade != student_grade:
                        studentFeedback("{:2s}{:10s}{:40s}{:10s}{:40s}".format("**", "", "Expected grade: {}".format(expected_grade), "", "Student grade: {}".format(student_grade)))
                        incorrect = True

                    if incorrect:
                        studentFeedback("\n")

            studentFeedback("\n\n")

            if incorrect:
                number_correct -= 1
                total_points_lost.append([self.deduction_dict[str(function_num)], "Incorrect output file content. See error messages above marked by *".format(function_name)])
                continue




    """
            ====================================================================
            ====================================================================
            ====================================================================
            ====================================================================
            ====================================================================
            ====================================================================
                       YOU SHOULD NOT NEED TO EDIT ANYTHING BELOW THIS
            --------====================================================--------
            ====================================================================
            ====================================================================
            ====================================================================
            ====================================================================
            ====================================================================
            ====================================================================
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
            submission_file_name = submission_finder.findSubmission(self.submission_directory_name, expected_file.strip(".cpp").strip(".h"), exact=self.exact_file_name)

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
        flattened_file_content_list = [item.strip() for file_i in self.student_files_content for item in file_i]
        self.student_files_content = flattened_file_content_list



    def check_functions(self):
        """Copies the student submission and changes their main method so that it can be compiled
        with a function checker program."""

        # Define required functions for checking in file and convert them to lower case
        check_required_functions = [self.split_function_string(func) for func in self.required_functions]



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

        # Check if the required number of functions list is non zero - this means some were not found in student file
        if number_of_found_functions != number_of_required_functions:
            # Iterate through required functions that were not found

            for required_function in check_required_functions:
                # Iterate through the full function named list to find the correct one for printing to student in deductions
                studentFeedback("\n")
                for full_req_fnx in self.required_functions:
                    full_req_fnx_check = ' '.join(self.split_function_string(full_req_fnx))

                    if ' '.join(required_function) == full_req_fnx_check:
                        studentFeedback("\tMISSING: {:s}".format(full_req_fnx))
                        self.make_deduction(self.missing_function_deduction, "{:s} function is required, but is missing from or incorrectly defined in your program. Correct this function for full credit.".format(full_req_fnx))
                        found_all_functions = False

                    else:
                        studentFeedback("\tFOUND: {:s}".format(full_req_fnx_check))

        # Print student feedback to inform of number required functions found
        studentFeedback("\n\tFound {} / {} required functions".format(number_of_found_functions, number_of_required_functions))

        return found_all_functions



    def split_function_string(self, function_string):
        #split on space , (, ), ',', and { then remove empty strings
        #but split on '//' first to remove comments
        parsed_function = re.split('\s|\(|\)|,|{', function_string)
        return [v for v in parsed_function if v != '']


    def match_function_string(self, user_func, expected_func_list):

        if len(user_func) == 0:
            return expected_func_list



        for required_func in expected_func_list:



            if len(user_func) != len(required_func):
                match = False
                continue

            match = True

            for (observed_word, expected_word) in zip(user_func, required_func):

                if observed_word not in expected_word or expected_word not in observed_word:
                    match = False
                    break

            if match:
                expected_func_list.remove(required_func)
                return expected_func_list


        return expected_func_list










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


        studentFeedback("\nGrading Deductions Summary")
        studentFeedback("==========================")

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
        print(max(self.final_grade, 0)) # THIS CANNOT BE DELETED!!!

        sys.stderr.write("______________________________________\n")
        sys.stderr.write("Score ---------------> {:0.2f}/{:0.2f}\n".format(max(0, self.final_grade), self.max_score))

        studentFeedback("\nGrading Note")
        studentFeedback("------------")
        studentFeedback("\t - You will receive a maximum of 50 points from COG.")
        studentFeedback("\t - The remaining 50 points will come from interview grading (30pts), your main function (10pts), and style (10pts).\n")
        studentFeedback("\nStyle Note")
        studentFeedback("------------")
        studentFeedback("\t - Make sure you properly comment your code!")
        studentFeedback("\t - Indent your code to make it readable. Use horizontal and vertical spacing accordingly.")
        studentFeedback("\t - See style notes in lecture notes/slides, assignment writeup, etc.\n")





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
