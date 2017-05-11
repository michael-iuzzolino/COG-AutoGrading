#!/usr/bin/env python3

"""
Author: Michael Louis Iuzzolino
Institution: University of Colorado Boulder

CSCI 1300 - Assignment 3 - Spring 2017
"""

import os,sys,inspect
import math
import numpy as np
import textwrap
import subprocess
import re

from modules.GradingUtilities import studentFeedback, compileCPPFile, generateTestData
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
        self.max_score = 60
        self.starting_grade = 60                                             # Set max grade



        self.expected_files = ["problem1.cpp", "problem2.cpp"]
        self.number_expected_files = len(self.expected_files)
        self.function_names = ["madLibs", "energyCalculator", "printEnergy", "calculateNumberHousesSupported"]

        # Define the required functions in their full name (for printing later)
        self.required_functions = ["void madLibs(void)",
                                   "double energyCalculator(double _, double _, double _, double _)",
                                   "void printEnergy(double _, double _, double _, double _)",
                                   "int calculateNumberHousesSupported(double _, double _)"]


        self.catch_phrases = ["In the book War of the ",
                              "The average annual solar energy production is ",
                              "The average annual solar energy for an efficiency of ",
                              " houses can be supported"]



        # Generate test_data
        self.test_input, self.test_output = generateTestData()

        # Set deductions
        self.missing_file_deduction = 90
        self.compile_fail_deduction = 100
        self.missing_function_deduction = 60
        self.incorrect_answer_deduction = 10
        self.incorrect_output_deduction = 4





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



        """
        Step 1: Check that the student's code compiles

            IF compile, go to step 2.
            ELSE: Deduct 100 points and EXIT.
        """
        studentFeedback("\n" + "="*100)
        studentFeedback("Checking Compile...", new_line=False),
        code_compiles = self.check_compile()

        if not code_compiles:
            self.make_deduction(self.compile_fail_deduction, "COG could not compile your file. Ensure the .cpp file compiles on your system.")
            studentFeedback("\tERROR! Does not compile!")
            return
            # EXIT

        studentFeedback("\tSuccess!")



        """
        Step 2: Create student_functions_file.cpp
        a. Change student's problem1.cpp main() to defunct()
        b. Copy each line of student's problem1.cpp into new file, student_functions_file.cpp, created at helper_folder_path
        """
        studentFeedback("\n" + "="*100)
        studentFeedback("Creating Alternate file...", new_line=False),
        self.create_altered_student_file()
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


        compileCPPFile(self.helper_file_path, helper_compiled_name, "Assignment File: {}".format(helper_compiled_name))
        studentFeedback("\tSuccess!")



        """
        Step 5: Run test cases
        """
        studentFeedback("\n" + "="*100)
        studentFeedback("Running Test Cases...\n"),
        self.test_cases(self.helper_file_path.replace(".cpp", ""))


        #
        # """
        # Step 6: Compare output files
        # """
        # solution_path_1 = os.getcwd() + "/helper/output/solution/solution_out_1.txt"
        # solution_path_2 = os.getcwd() + "/helper/output/solution/solution_out_2.txt"
        # student_path_1 = os.getcwd() + "/helper/output/student/out1.txt"
        # student_path_2 = os.getcwd() + "/helper/output/student/out2.txt"
        #
        # self.check_output_file(solution_path_1, student_path_1, 1)
        # self.check_output_file(solution_path_2, student_path_2, 2)
        #
        #





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

            compiled_program_name = submission_file.replace(".cpp", "")
            program_compiles = compileCPPFile(submission_file, compiled_program_name, "Assignment File: {}".format(assignment_name))


            if not program_compiles:
                self.make_deduction(self.compile_fail_deduction, "{} does not compile. Check your coding with c++11 standard.".format(assignment_name))
                return False

        return True



    def write_helper(self):
        # Sets paths for LOCAL SYSTEM TESTS
        if self.local_system_test:
            self.helper_file_path = "helper/helper.cpp"
            self.defunct_student_file_paths = ["helper/student_functions_file_{}.cpp".format(i+1) for i in range(self.number_expected_files)]

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
            self.defunct_student_file_paths = [self.submission_directory_name + "/student_functions_file_{}.cpp".format(i+1) for i in range(self.number_expected_files)]





    def create_altered_student_file(self):

        # Setup helper file
        self.write_helper()

        for index, (assignment_path, assignment_name) in enumerate(zip(self.student_files_path, self.student_file_names)):

            # Open the student's submitted assignment file and create a defunct_student_file in the helper file path to copy to
            with open(assignment_path, "r") as student_file, open(self.defunct_student_file_paths[index], "w") as defunct_student_file:
                # Read each line of the student file
                for line in student_file:

                    # If main is found, replace main with defunct - this enables us to call the file as a library from our helper file
                    if ("int main()".replace(" ","") in line.lower().replace(" ", "")) or ("int main(void)".replace(" ", "") in line.lower().replace(" ", "")):
                        line = line.replace("main", "defunct{}".format(index))
                        main_found = True

                    # Write the line (or new defunct line) to the defunct student file
                    defunct_student_file.write(line)

            # Open the student's file again, read all lines, and save to the student files content list
            with open(assignment_path, "r") as student_file:
                self.student_files_content.append(student_file.readlines())

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





    def parse_student_answers(self, student_answers):
        # https://automatetheboringstuff.com/chapter7/
        answers_string = " ".join(student_answers)

        # http://stackoverflow.com/questions/12683201/python-re-split-to-split-by-spaces-commas-and-periods-but-not-in-cases-like
        answers_list = re.split(':|(?<!\d)[.](?!\d)', answers_string)


        new_answers = []
        for answers in answers_list:
            answer = answers.strip()
            for catch_phrase in self.catch_phrases:
                if catch_phrase.lower() in answer.lower():
                    new_answers.append(answer+".")
        return new_answers



    def test_cases(self, helper_path):

        points_lost = []
        expected_outputs = self.test_output

        # Starts process
        argv_cwd = os.getcwd() + "/helper/"
        argv1 = argv_cwd + "/output/student/out1.txt"
        argv1 = argv1.replace("//", "/")

        full_argv_path = argv1
        final_path = helper_path + " " + full_argv_path
        process = subprocess.Popen(final_path, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=sys.stderr, shell=True)


        # Build inputs to send
        input_feed = self.test_input

        # Sending inputs and receiving outputs and errs
        out, err = process.communicate(("\n".join(input_feed)).encode(), timeout=10) # Pass inputs and receive outputs and errs

        # Splits the console output by newline character into a list of all outputs
        student_answers = out.decode().split("\n")

        # Clean student answers from empty newlines at very end of program; e.g., very last cout has endl; this is fine!
        if student_answers[-1] == '':
            student_answers = student_answers[:-1]


        # Parse out student answers!
        student_answers = self.parse_student_answers(student_answers)

        # Check for correct answers
        num_student = len(student_answers)
        num_expected = len(expected_outputs)
        if num_student != num_expected:

            points_lost.append([self.incorrect_answer_deduction, "Incorrect number of outputs. Your file should print {} outputs; you have {} outputs. Check for correct formatting of output string!".format(num_expected, num_student)])


        for index, (expected_answer, student_answer) in enumerate(zip(expected_outputs, student_answers)):

            if index < 3:
                function_name_index = 0
            else:
                function_name_index = 1

            # studentFeedback("{:30s}Checking your function, '{:s}'...".format("", self.function_names[function_name_index])) if index%3 == 0 else studentFeedback("")
            expected = expected_answer.replace(" ", "").lower()
            student = student_answer.replace(" ", "").lower()

            if self.function_names[function_name_index] == "madLibs":
                studentFeedback("{:2s}{}".format("**" if expected != student else "", "Expected Output"))
                studentFeedback("{:2s}{}".format("", "---------------"))
                studentFeedback("\t{}\n".format(textwrap.fill(expected_answer, 90)))

                studentFeedback("{:2s}{}".format("**" if expected != student else "", "Your Ouput"))
                studentFeedback("{:2s}{}".format("", "----------"))
                studentFeedback("\t{}\n".format(textwrap.fill(student_answer, 90)))

                if expected != student:
                    points_lost.append([10, "Incorrect Answer. Expected Output: {:30s}, Your Output: {:30s}".format(expected_answer, student_answer)])

                studentFeedback("\n")

            else:
                studentFeedback("{:6s}{:70s}{:10s}{:70s}".format("", "Expected Output", "", "Your Ouput"))
                studentFeedback("{:6s}{:70s}{:10s}{:70s}".format("", "---------------", "", "----------"))
                if expected != student:
                    studentFeedback("{:4s}{:2s}{:70s}{:10s}{:70s}{:2s}".format("", "**", expected_answer, "", student_answer, "**"))
                    points_lost.append([10, "Incorrect Answer. Expected Output: {:30s}, Your Output: {:30s}".format(expected_answer, student_answer)])
                else:
                    studentFeedback("{:6s}{:70s}{:10s}{:70s}{:2s}".format("", expected_answer, "", student_answer, ""))
                studentFeedback("\n\n")


        for point_lost in points_lost:
            self.make_deduction(point_lost[0], point_lost[1])




    def check_output_file(self, student_outfile_path, solution_outfile_path, test_number):
        # Get students output file
        with open(student_outfile_path, "r") as student_outfile:
            student_file = student_outfile.readlines()

        with open(solution_outfile_path, "r") as solution_outfile:
            solution_file = solution_outfile.readlines()

        self.check_output(student_file, solution_file, test_number)


    def check_output(self, solution_outfile, student_outfile, test_number):
        studentFeedback("\n")
        studentFeedback("\t\t\tTestcase {}".format(test_number))
        studentFeedback("\t\t\t===========\n")
        studentFeedback("{:2s} \t {:20s} \t {:20s} {:2s}".format("  ", "Expected Line", "Student Line", "  "))
        studentFeedback("{:2s} \t  ------------- \t\t ------------ {:2s}".format("  ", "  "))


        for expected_line, student_line in zip(solution_outfile, student_outfile):

            if expected_line != student_line:
                studentFeedback("{:2s} \t {1:20s} \t {2:20s} {:2s} ".format("**", textwrap.fill(expected_line.strip(), 20), student_line.strip(), "**  INCORRECT"))
                self.make_deduction(self.incorrect_output_deduction, "Incorrect output. Expected output {} vs. Your Output: {}".format(expected_line, student_line))
            else:
                studentFeedback("{:2s} \t {:20s} \t {:20s} {:2s}".format("  ", expected_line.strip(), student_line.strip(), "  "))

        studentFeedback("\n\n")











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
        sys.stderr.write("Remaining 40% of your score will come from the interview grading.")




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
