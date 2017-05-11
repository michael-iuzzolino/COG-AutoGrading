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

from modules.GradingUtilities import studentFeedback, compileCPPFile
from modules import SubmissionFinder
from modules.testcases import generate_test_cases


class GradeSubmission():

    def __init__(self, submission_directory, COG_script_directory, local_test=False):
        """
            Constructor
        """
        if local_test:
            self.COG_home_dir = COG_script_directory
            self.infile_dir = COG_script_directory + "/files/"
            self.infile_dir.replace("//", "/")
        else:
            self.COG_home_dir = COG_script_directory + "/COG/"
            self.COG_home_dir.replace("//", "/")
            self.infile_dir = COG_script_directory + "/COG/files/"
            self.infile_dir.replace("//", "/")

        os.chdir(self.COG_home_dir)                                   # Changes current working directory to given path; returns None in all the cases

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
        self.starting_grade = self.max_score                                              # Set max grade


        # File names
        self.expected_files = ["main.cpp", "SpellChecker.h", "SpellChecker.cpp", "WordCounts.h", "WordCounts.cpp"]
        self.compile_files = ["main.cpp", "SpellChecker.cpp", "WordCounts.cpp"]
        self.test_1_compile_files = ["helper_1.cpp", "SpellChecker.cpp"]
        self.test_2_compile_files = ["helper_2.cpp", "WordCounts.cpp"]

        self.move_files = ["SpellChecker.h", "SpellChecker.cpp", "WordCounts.h", "WordCounts.cpp"]
        self.exact_file_name = True;

        self.number_expected_files = len(self.expected_files)
        self.number_expected_helper_files = len(self.compile_files)

        self.input_file_list = ["GONE_FOREVER.txt",
                                "GOODALL.txt",
                                "MISSPELLED.txt",
                                "TEXT_2_ENGLISH.txt",
                                "VALID_WORDS_3000.txt"]


        # Setup read-write location
        if self.local_system_test:
            self.write_file_path = "files/"
        else:
            self.write_file_path = self.submission_directory_name + "/"


        # Function names
        self.function_names = []


        # Define the required functions in their full name (for printing later)
        self.required_functions = {"SpellChecker" : ["SpellChecker::SpellChecker()",
                                                     "SpellChecker::SpellChecker(string lang)",
                                                     "SpellChecker::SpellChecker(string lang, string valid_words_filename, string misspelled_filename)",
                                                     "bool SpellChecker::loadValidWords(string filename)",
                                                     "bool SpellChecker::loadMisspelledWords(string filename)",
                                                     "void SpellChecker::setBeginMarker(char begin)",
                                                     "void SpellChecker::setEndMarker(char end)",
                                                     "char SpellChecker::getBeginMarker()",
                                                     "char SpellChecker::getEndMarker()",
                                                     "string SpellChecker::fixUp(string sentence)"],
                                   "WordCounts" : ["WordCounts::WordCounts()",
                                                   "void WordCounts::countWords(string sentence)",
                                                   "int WordCounts::getCount(string word)",
                                                   "void WordCounts::resetCounts()",
                                                   "int WordCounts::mostCommon(string commonWords[], int wordCount[], int n)"] }


        # Generate test cases
        self.__generate_test_cases()

        # Catch phrases for parsing student output
        self.catch_phrases = []



        # Set deductions
        self.missing_file_deduction = self.max_score
        self.compile_fail_deduction = self.max_score
        total_functions = len(self.required_functions['SpellChecker']) + len(self.required_functions['WordCounts'])
        self.missing_function_deduction = self.max_score / total_functions * 2.2
        self.no_answer_deduction = self.max_score

        self.deduction_dict = {"1" : 5,     # 1 test case, 5 pts each
                               "2" : 5,      # 3 test cases, 5 pts each
                               "3" : 10}     # 3 test cases, 10 pts each



    def __generate_test_cases(self):
        self.test_case_dict, self.test_case_num_to_description = generate_test_cases()



    def parse_student_answers(self, student_answers, test_number):
        # https://automatetheboringstuff.com/chapter7/

        new_answers = []
        for answers in student_answers:
            answer = answers.strip()
            for catch_phrase in self.catch_phrases:
                if catch_phrase.lower() in answer.lower():
                    new_answers.append(answer)

        return new_answers



    def run_test_case(self, class_test, test_case_num, test_case):

        test_case_description = self.test_case_num_to_description[class_test][test_case_num]
        test_passed = True

        studentFeedback("{} Class: Testcase {} -- {}".format(class_test, test_case_num, test_case_description))
        studentFeedback("{}----------------------{}\n".format("-"*len(class_test), "-"*len(test_case_description)))


        program_name = "./test_1" if class_test == "SpellChecker" else "./test_2"

        total_points_lost = []

        input_feed = test_case["input"]
        expected_outputs = test_case["output"]


        # Starts process
        process = subprocess.Popen(program_name, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=sys.stderr, shell=True)

        # Sending inputs and receiving outputs and errs
        out, err = process.communicate(("\n".join(input_feed)).encode(), timeout=10) # Pass inputs and receive outputs and errs


        # Splits the console output by newline character into a list of all outputs
        try:
            student_answers = out.decode().split("\n")
        except:
            num_points_lost = 10
            test_case_description = "** Your program is not producing output for this testcase. Check the function corresponding to this testcase for correct functionality."
            studentFeedback(test_case_description)
            total_points_lost.append([num_points_lost, "Incorrect output in {}'s {}.".format(class_test, test_case_description)])
            return

        # Clean student answers from empty newlines at very end of program; e.g., very last cout has endl; this is fine!
        if student_answers[-1] == '':
            student_answers = student_answers[:-1]

        # print("expected_outputs: {}".format(expected_outputs))
        # print("student_answers: {}\n".format(student_answers))

        if len(student_answers) != len(expected_outputs):
            studentFeedback("Incorrect number of outputs.")

        for expected, student in zip(expected_outputs, student_answers):
            if expected != student.replace("  ", " ").strip():
                test_passed = False
                num_points_lost = 10
                total_points_lost.append([num_points_lost, "Incorrect output in {}'s {}.".format(class_test, test_case_description)])

        if test_passed:
            studentFeedback("   {} passed all tests.".format(test_case_description))
        else:
            studentFeedback("** {} failed to pass tests.".format(test_case_description))

        studentFeedback("\n\n")


        # DEDUCT POINTS
        for point_lost in total_points_lost:
            self.make_deduction(point_lost[0], point_lost[1])




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



        """
        Step 1: Check that the student's code compiles

            IF compile, go to step 2.
            ELSE: Deduct 100 points and EXIT.
        """

        studentFeedback("\n" + "="*100)
        studentFeedback("\n\tChecking Compile", new_line=True),
        studentFeedback("\t================")
        code_compiles = self.check_compile()
        os.chdir(self.COG_home_dir)
        if not code_compiles:
            self.make_deduction(self.compile_fail_deduction, "COG could not compile your file. Ensure the .cpp file compiles on your system.")
            studentFeedback("\tERROR! Does not compile!")
            return
            # EXIT

        studentFeedback("\nSuccessful Compile. Address warnings, if any.")



        """
        Step 2: Create student_functions_file.cpp
        a. Change student's problem1.cpp main() to defunct()
        b. Copy each line of student's problem1.cpp into new file, student_functions_file.cpp, created at helper_folder_path
        """
        studentFeedback("\n" + "="*100)
        studentFeedback("Creating Alternate file...", new_line=False),
        self.move_helper_files()
        studentFeedback("\tSuccess!")



        # """
        # Step 3: Check that all required functions exist
        #     IF all required functions, go to step 3.
        #     ELSE: Deduct 1 / number_required_functions per missing function, then EXIT.
        # """
        studentFeedback("\n" + "="*100)
        studentFeedback("Checking for Required Functions... "),
        found_functions = self.check_functions()

        counter = 0
        for class_name, found_function in found_functions.items():
            if not found_function:
                counter += 1

        if counter == len(found_functions):

            studentFeedback("\tERROR: Could not find all required functions. Ensure you are using void in function definitions as specified in assignment writeups.")
            return
            # EXIT




        # """
        # Step 4: Compile helper.cpp
        # IMPORTANT: Be sure to pass it input_name_1, input_name_2, output_name_1, and output_name_2 for argv
        # """
        # studentFeedback("\n" + "="*100)
        # studentFeedback("Creating Helper.cpp file...", new_line=False),

        os.chdir(self.submission_directory_name)
        submission_file_names = " ".join(self.test_1_compile_files)
        compiled_program_name = "test_1"
        program_compiles = compileCPPFile(submission_file_names, compiled_program_name)

        submission_file_names = " ".join(self.test_2_compile_files)
        compiled_program_name = "test_2"
        program_compiles = compileCPPFile(submission_file_names, compiled_program_name)




        # """
        # Step 5: Run test cases
        # """
        studentFeedback("\n" + "="*100)
        studentFeedback("Running Test Cases...\n"),
        for class_test, test_cases in self.test_case_dict.items():
            for test_case_num, test_case in test_cases.items():
                self.run_test_case(class_test, test_case_num, test_case)






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
            submission_file_name = submission_finder.findSubmission(self.submission_directory_name, expected_file, exact=True)

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
        studentFeedback("\nCompile Errors and Warnings")
        studentFeedback("---------------------------")
        submission_file_list = []
        # Iterate through submission files (if numerous .cpp in .zip file)
        for submission_file, assignment_name in zip(self.student_files_path, self.student_file_names):
            if assignment_name in self.compile_files:
                submission_file_list.append(assignment_name)

        os.chdir(self.submission_directory_name)
        submission_file_names = " ".join(submission_file_list)
        compiled_program_name = "test_submission_compile"
        program_compiles = compileCPPFile(submission_file_names, compiled_program_name)


        if not program_compiles:
            self.make_deduction(self.compile_fail_deduction, "{} does not compile. Check your coding with c++11 standard.".format(assignment_name))
            return False

        return True




    def write_helper(self):
        if self.local_system_test:
            pass

        self.helper_file_path = []
        for i in range(1, 3):
            current_helper_path = self.COG_home_dir + "/helper_{}.cpp".format(i)
            submission_write_path = self.submission_directory_name + "/helper_{}.cpp".format(i)
            submission_write_path = submission_write_path.replace("//", "/")


            # Rewrite helper files into submission dir
            with open(current_helper_path, "r") as infile, open(submission_write_path, "w") as outfile:
                for line in infile:
                    outfile.write(line)


    def move_input_files(self):
        for infile in self.input_file_list:
            current_file_path = self.infile_dir + "/" + infile
            current_file_path.replace("//", "/")

            submission_write_path = self.submission_directory_name + "/{}".format(infile)
            submission_write_path = submission_write_path.replace("//", "/")

            with open(current_file_path, "r") as infile, open(submission_write_path, "w") as outfile:
                for line in infile:
                    outfile.write(line)



    def move_helper_files(self):
        # Setup helper file
        self.write_helper()
        self.move_input_files()

        self.student_files_content = {"SpellChecker" : [], "WordCounts" : []}

        index = 0
        for assignment_path, assignment_name in zip(self.student_files_path, self.student_file_names):

            if assignment_name not in self.move_files:
                continue

            name = assignment_name.strip(".cpp").strip(".h")

            # # Rewrite the student's file to correct place
            # with open(assignment_path, "r") as student_file, open(self.student_helper_file_paths[index], "w") as student_helper_file:
            #     for line in student_file:
            #         student_helper_file.write(line)

            # Open the student's file again, read all lines, and save to the student files content list
            with open(assignment_path, "r") as student_file:
                self.student_files_content[name].append(student_file.readlines())

            index += 1


        # Flatten the file content list
        flattened_file_spellchecker = [item.strip() for file_i in self.student_files_content['SpellChecker'] for item in file_i]
        self.student_files_content['SpellChecker'] = flattened_file_spellchecker

        flattened_file_wordcounts = [item.strip() for file_i in self.student_files_content['WordCounts'] for item in file_i]
        self.student_files_content['WordCounts'] = flattened_file_wordcounts



    def check_functions(self):
        """Copies the student submission and changes their main method so that it can be compiled
        with a function checker program."""
        found_functions = {}
        for class_name, required_functions in self.required_functions.items():
            studentFeedback("\nChecking {} class functions...\n".format(class_name))
            student_file_content = self.student_files_content[class_name]
            found_functions[class_name] = True

            # Define required functions for checking in file
            check_required_functions = [self.split_function_string(func) for func in required_functions]



            number_of_required_functions = len(required_functions)   # Define number of required functions
            number_of_found_functions = 0                            # Define number of required functions found in the given file



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

                    for full_req_fnx in required_functions:
                        full_req_fnx_check = ' '.join(self.split_function_string(full_req_fnx))

                        if ' '.join(required_function) == full_req_fnx_check:
                            studentFeedback("\tMISSING: {:s}".format(full_req_fnx))
                            self.make_deduction(self.missing_function_deduction, "{:s} function is required, but is missing from or incorrectly defined in your program. Correct this function for full credit.".format(full_req_fnx))
                            found_functions[class_name] = False


            # Print student feedback to inform of number required functions found
            studentFeedback("\n\tFound {} / {} required functions".format(number_of_found_functions, number_of_required_functions))

        return found_functions



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
