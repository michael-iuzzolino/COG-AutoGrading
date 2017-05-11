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
import re, time
import json

from modules.GradingUtilities import studentFeedback, progress_update
from modules import SubmissionFinder
from modules.testcases import generate_test_cases
from subprocess import CalledProcessError, check_output
# from termcolor import colored

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
        self.expected_files = ["assignment10.py"]
        self.helper_files = ["helper.py"]


        self.number_expected_files = len(self.expected_files)


        self.input_file_list = ["books.txt", "ratings.txt"]


        # Setup read-write location
        if self.local_system_test:
            self.write_file_path = "files/"
        else:
            self.write_file_path = self.submission_directory_name + "/"


        # Function names
        self.function_names = []


        # Define the required functions in their full name (for printing later)
        self.required_functions = ["class Recommender",
                                   "def read_books",
                                   "def read_users",
                                   "def calculate_average_rating",
                                   "def lookup_average_rating",
                                   "def calc_similarity",
                                   "def get_most_similar_user",
                                   "def recommend_books"]


        # Generate test cases
        self.test_cases_list = generate_test_cases()


        # Set deductions
        self.missing_file_deduction = self.max_score
        self.compile_fail_deduction = self.max_score
        total_functions = len(self.required_functions)
        self.missing_function_deduction = self.max_score / total_functions * 2.2
        self.no_answer_deduction = self.max_score

        self.deduction_dict = {"1" : 5,     # 1 test case, 5 pts each
                               "2" : 5,      # 3 test cases, 5 pts each
                               "3" : 10}     # 3 test cases, 10 pts each





    def parse_student_answers(self, student_answers, test_number):
        # https://automatetheboringstuff.com/chapter7/

        new_answers = []
        for answers in student_answers:
            answer = answers.strip()
            for catch_phrase in self.catch_phrases:
                if catch_phrase.lower() in answer.lower():
                    new_answers.append(answer)

        return new_answers



    def run_test_case(self, test_case_num, test_case_name, test_case_IO):

        # Print testing header
        studentFeedback("Test Case {}".format(test_case_num))
        studentFeedback("----------{}".format("-"*len(str(test_case_num))))
        studentFeedback("\n\tTesting {}...\n".format(test_case_name))

        # Set input and output_expected
        input_feed = str(test_case_IO["input"])+"\n"
        expected_outputs = test_case_IO["output"]

        # Initialize points lost list
        total_points_lost = []

        # Change directory to submission directory
        os.chdir(self.submission_directory_name)


        # Starts process
        process = subprocess.Popen(["python", "helper.py", "books.txt", "ratings.txt"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=sys.stderr, shell=False)

        # Communicate with process and retrieve output
        out, err = process.communicate(input_feed.encode(), timeout=10)

        # Check if error occurred
        if process.returncode != 0:
            # Print error message
            error_string = "* * * Error with your program. See Tracback above for debugging suggestions. * * *"
            studentFeedback("\n")
            studentFeedback("\t" + "*" * len(error_string))
            studentFeedback("\t" + error_string)
            studentFeedback("\t" + "*" * len(error_string))
            studentFeedback("\n")
            studentFeedback("\n")

            # Deduct points
            self.make_deduction(10, "Runtime error! {} produces a runtime error. Check for syntax or logics errors. See Traceback above for debugging suggestions.".format(test_case_name))

            # Return
            return False

        # Define student answers
        student_answers = out.decode().split("\n")

        no_answers = False
        # Check if student answer is empty:
        if len(student_answers) == 0:
            no_answers = True
        elif len(student_answers) == 1 and len(student_answers[0]) == 0:
            no_answers = True

        if no_answers:
            self.make_deduction(10, "Error with {}".format(test_case_name))
            return False

        # Clean empty string off end of list
        if len(student_answers[-1]) == 0:
            student_answers = student_answers[:-1]




        # Check student vs. expected answer
        for index, (student_answer, expected_answer) in enumerate(zip(student_answers, expected_outputs)):



            if test_case_num == 0:

                print("\tChecking for correct number of Recommender class members...")
                # print("Number of class members in STUDENT's file: {}\n".format(student_answer))
                # print("Expected number of class members: {}\n".format(expected_answer))


                if student_answer != expected_answer:
                    studentFeedback("\n\t** Incorrect. Found {} class members. Expected 3.".format(student_answer))
                    self.make_deduction(10, "__init__ test incorrect. Your class should have 3 members.")
                else:
                    studentFeedback("\n\t  Correct! Found necessary number of class members.\n")




            elif test_case_num == 1 or test_case_num == 2:

                if index == 0:
                    print("\tSubtest 1: Checking for correct handling of invalid input text file...")
                    # print("\t\t Student's return value: {}\n".format(student_answer))
                    # print("\t\t Expected return value: {}\n".format(expected_answer))

                    if student_answer != str(expected_answer):
                        studentFeedback("\t** Incorrect. Your file's output: {}".format(student_answer))
                        studentFeedback("\t** Refer to writeup for correct handling of invalid filenames.")
                        self.make_deduction(10, "Incorrect output for {}".format(test_case_name))
                    else:
                        studentFeedback("\t  Correct!\n")
                else:
                    print("\n\tSubtest 2: Checking for successful open of input file and the return of appropriate dictionary.")
                    if student_answer == str(expected_answer):
                        studentFeedback("\t  Correct!\n")

                        # print("\t\t Student's return: {}\n".format(student_answer[:100] + " ..."))
                        # print("\t\t Expected return: {}\n".format(str(expected_answer)[:100] + " ..."))

                    else:

                        json_acceptable_string = student_answer.replace("'", "\"")
                        try:
                            js = json.loads(json_acceptable_string)
                            if js == expected_answer:
                                studentFeedback("\t  Correct!\n")
                            else:
                                studentFeedback("\t** Incorrect.")
                                self.make_deduction(10, "Incorrect output for {}. Check writeup for correct dictionary structure.".format(test_case_name))

                            # print("\t\t Student's return: {}\n".format(str(js)[:100] + " ..."))
                            # print("\t\t Expected return: {}\n".format(str(expected_answer)[:100] + " ..."))

                        except Exception as e:
                            studentFeedback("\t** Incorrect. Check writeup for correct dictionary structure.")
                            studentFeedback("\t** Your output: {}\n".format(student_answer[:50] + " ..."))
                            self.make_deduction(10, "Incorrect output for {}. Check writeup for correct dictionary struture.".format(test_case_name))

                            # print("\t\t Student's return value: {}\n".format(student_answer[:50] + " ..."))
                            # print("\t\t Expected return value: {}\n".format(str(expected_answer)[:50] + " ..."))


            # Similarity test
            elif test_case_num == 3 or test_case_num == 4:

                if test_case_num == 3:
                    studentFeedback("\tChecking similary method between random user {} and user {}...".format(np.random.randint(1, 5), np.random.randint(6, 13)))
                    if index == 0:
                        user1 = "Albus_Dumbledore"
                        user2 = "Harry_Potter"
                    else:
                        user1 = "YJAM"
                        user2 = "Apollo"

                    # print("\t\t Input:  User 1: {} \t User 2: {}\n".format(user1, user2))

                elif test_case_num == 4:
                    studentFeedback("\tSearching for the most similar user to user {}...".format(np.random.randint(1, 23)))
                    user1 = "Albus_Dumbledore"

                    # print("\t\t Input:  User 1: {}\n".format(user1))

                #
                #
                # print("\t\t Student's return: {}\n".format(student_answer))
                # print("\t\t Expected return: {}\n".format(expected_answer))

                if student_answer == expected_answer:
                    studentFeedback("\t  Correct!\n")
                else:
                    studentFeedback("\t** Incorrect. Ensure you are calculating similarity correctly.\n\n")
                    studentFeedback("\t** Your output: {}\n\n".format(student_answer))
                    self.make_deduction(10, "Incorrect output for {}. Your output: {}. Ensure you are calculating similarity correctly.".format(test_case_name, student_answer))

            # Recommend books
            elif test_case_num == 5:
                studentFeedback("\tChecking recommended books for random user {}...".format(np.random.randint(1, 20)))
                if index == 0:
                    user1 = "Albus_Dumbledore"
                else:
                    user1 = "NaRwHaLs"

                # print("\t\t Input:  User 1: {}\n".format(user1))
                #
                # print("\t\t Student's return: {}\n".format(student_answer))
                # print("\t\t Expected return: {}\n".format(expected_answer))

                if student_answer == expected_answer:
                    studentFeedback("\t  Correct!\n")
                else:
                    studentFeedback("\t** Incorrect.\n\n")
                    self.make_deduction(10, "Incorrect output for {}".format(test_case_name))



        studentFeedback("\n\n")







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



    """
            ====================================================================
                                    MAIN SEQUENCE
            ====================================================================
    """
    def run_main_grading_sequence(self):


        self.print_header()

        """
        Step 0.a: Locate student's submission
            IF all submissions found, go to step 1.
            ELSE, deduct 100 points and EXIT.
        """
        studentFeedback("\n" + "="*100)
        studentFeedback("Locating Submission...")
        # # progress_update  ()
        found_submission = self.locate_submissions()

        if not found_submission:
            studentFeedback("\t\t\tCould not locate submission.")
            self.make_deduction(100, "Could not locate submission.")
            return
            # EXIT
        studentFeedback("\t\t\tSuccess!")



        """
        Step 1: Remove print statements from student file
        """

        studentFeedback("\n" + "="*100)
        studentFeedback("\nProcessing student file...", new_line=True),
        proper_file = self.process_student_file()
        os.chdir(self.COG_home_dir)

        if proper_file:
            studentFeedback("\n\tSuccess.")
        else:
            studentFeedback("\n\tFailed.")
            self.make_deduction(100, "Could not find if __name__ == '__main__': in your file.")
            return


        """
        Step 2: Create student_functions_file.cpp
        a. Change student's problem1.cpp main() to defunct()
        b. Copy each line of student's problem1.cpp into new file, student_functions_file.cpp, created at helper_folder_path
        """
        studentFeedback("\n" + "="*100)
        studentFeedback("\nMigrating Files...", new_line=True),
        studentFeedback("\n\t1. Helper file...", new_line=True),
        self.write_helper()
        # # progress_update  ()

        studentFeedback("\n\t2. Text files...", new_line=True),
        self.move_input_files()
        # progress_update  ()

        # self.move_helper_files()
        studentFeedback("\tSuccess!")



        """
        Step 3: Check that all required functions exist
            IF all required functions, go to next step.
            ELSE exit
        """
        studentFeedback("\n" + "="*100)
        studentFeedback("\nChecking for Required Class and Functions... "),
        found_all_functions = self.check_functions()

        if found_all_functions:
            studentFeedback("\tSuccess.")
        else:
            studentFeedback("\tERROR: Could not find all required functions. Ensure you are using void in function definitions as specified in assignment writeups.")
            return


        """
        Step 4:
        """
        studentFeedback("\n" + "="*100)
        studentFeedback("\nRunning Test Cases...\n"),
        for test_case_num, test_case in enumerate(self.test_cases_list):
            for test_case_name, test_case_IO in test_case.items():
                successful = self.run_test_case(test_case_num, test_case_name, test_case_IO)


    """
            ====================================================================
                                    END MAIN SEQUENCE
            ====================================================================
    """




    def print_header(self):
        with open("header.txt", "r") as infile:
            for line in infile:
                studentFeedback(line.strip("\n"))




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
                self.make_deduction(self.missing_file_deduction, "Could not locate your {} file. Ensure your file is correctly named and zipped.".format(expected_file))

        studentFeedback("\n\t{}/{} files successfully located.".format(number_files_found, self.number_expected_files))
        return found_some_files



    def process_student_file(self):

        # Setup file paths
        original_filename = self.expected_files[0]
        cleaned_filename = original_filename.replace(".py", "_cleaned.py")

        submission_read_path = self.submission_directory_name + "/{}".format(original_filename)
        submission_read_path = submission_read_path.replace("//", "/")

        submission_write_path = self.submission_directory_name + "/{}".format(cleaned_filename)
        submission_write_path = submission_write_path.replace("//", "/")

        # Open student's file and read it into student_file object
        with open(submission_read_path, "r") as infile:
            student_file = infile.readlines()

        # Set student file content
        self.student_files_content = student_file

        studentFeedback("\n\t1. Checking for: 'if __name__ == '__main__': \n\t\t\t  main()", new_line=True),
        studentFeedback("\t", new_line=True),
        # progress_update  ()


        # Check for if __name__
        found_dunder_name = False
        for line in student_file:
            if "__name__" in line:
                found_dunder_name = True
                break

        if not found_dunder_name:
            return False


        # Replace print statements with comment
        studentFeedback("\n\t2. Replacing print statements...", new_line=True),
        studentFeedback("\t", new_line=True),
        # progress_update  ()

        student_outfile = [line.replace("print", "pass #") for line in student_file]
        
        # Create new student file with print statements replaced
        studentFeedback("\n\t3. Rewriting student submission...", new_line=True),
        studentFeedback("\t", new_line=True),
        # progress_update  ()
        with open(submission_write_path, "w") as outfile:
            for new_out in student_outfile:
                outfile.write(new_out)

        return True


    def write_helper(self):
        if self.local_system_test:
            pass

        current_helper_path = self.COG_home_dir + "/helper.py"
        submission_write_path = self.submission_directory_name + "/helper.py"
        submission_write_path = submission_write_path.replace("//", "/")

        # Rewrite helper files into submission dir
        with open(current_helper_path, "r") as infile, open(submission_write_path, "w") as outfile:
            for line in infile:
                outfile.write(line)

        # Write __init__.py file
        init_write_path = self.submission_directory_name + "/__init__.py"
        init_write_path = init_write_path.replace("//", "/")
        with open(init_write_path, "w") as outfile:
            outfile.write("")


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

            name = assignment_name.strip(".py")

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

        functions_found = 0
        total_required_functions = len(self.required_functions)
        found_all_functions = False

        for required_function in self.required_functions:
            studentFeedback("\n\tChecking: \t '{}'\n".format(required_function))
            # progress_update  (time_step=0.01)

            found_function = False
            for student_line in self.student_files_content:

                if required_function in student_line:
                    print("\t\tFound!\n")
                    found_function = True
                    functions_found += 1
                    break

            if not found_function:
                studentFeedback("\t\t** Function NOT Found!\n")
                self.make_deduction(1/len(self.required_functions)*100, "{} not found.".format(required_function))

        if functions_found == total_required_functions:
            found_all_functions = True


        studentFeedback("\n")
        studentFeedback("\t\t***************************\n")
        studentFeedback("\t\t| Found {:2d} /{:2d} functions. |\n".format(functions_found, total_required_functions))
        studentFeedback("\t\t***************************\n")

        return found_all_functions














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
