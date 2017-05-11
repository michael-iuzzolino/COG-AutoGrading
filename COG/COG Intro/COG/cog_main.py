#!/usr/bin/env python3

"""
Author: Michael Louis Iuzzolino
Institution: University of Colorado Boulder
"""

#CSCI 1300 - Assignment 2 Grader
#THESE LINES ARE NEEDED TO ADD THE GradingScriptLibrary path to the system path so they can be imported!!!
import os,sys,inspect
import json
import math
import time


cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../../../")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
#DO NOT DELETE THE LINES ABOVE

import subprocess
import glob
import re
import shutil
import codecs
from GradingScriptLibrary.GradeUtils import studentFeedback,getAllNumbersFromString,remove_control_chars#,stringContainsCorrecthreerds_WillHandleMispellings
from GradingScriptLibrary.GradeUtils import appendToBeginningOfFile
from GradingScriptLibrary.CPPHelpers import CPPCompiler
from GradingScriptLibrary.CPPHelpers.CPPProgramRunner import CPPProgramRunner
from GradingScriptLibrary.SeedFileLoader import SeedFileLoader
from GradingScriptLibrary import GradeUtils
from GradingScriptLibrary import SubmissionFinder
anyNumberRE =  re.compile("([-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?)")


class GradeSubmission():

    def __init__(self, submission_directory_name, script_directory):
        """
            Constructor
        """

        os.chdir(script_directory)                                   # Changes current working directory to given path; returns None in all the cases
        self.submission_directory_name = submission_directory_name      # Sets up
        self.deductions = []
        self.location_of_files = []
        self.assignment_names = []
        self.student_files = []

        self.expected_files = ["recitation2.cpp"]




        """
        Step 0.a: Locate student's submission
            IF all submissions found, go to step 1.
            ELSE, deduct 100 points and EXIT.
        """
        studentFeedback("Locating Submission...")
        found_submission = self.locate_submission()

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
        studentFeedback("\nChecking Compile..."),
        code_compiles = self.check_compile()

        if not code_compiles:
            self.make_deduction(self, 100, "COG could not compile your file. Ensure the .cpp file compiles on your system.")
            studentFeedback("\t\t\tDoes not compile.")
            return
            # EXIT

        studentFeedback("\t\t\tSuccess!")




        """
        Step 2: Generate Data for helper.cpp test cases
        """
        self.generate_test_data()


        """
        Step 3: Run test cases
        """
        studentFeedback("\nRunning Test Cases..."),
        self.test_cases(self.submission_directory_name.replace(".cpp", ""))









    def locate_submission(self):
        """
            Docstring Under Construction
            Find the submission in the folder - sometimes it isn't named exactly
        """

        submission_finder = SubmissionFinder.SubmissionFinder()      # Creates submissionFinder object

        # Iterates through expected file names and checks if each are in the submissions directory
        found_all_files = True
        for index, expected_file in enumerate(self.expected_files):
            submission_file_name = submission_finder.findSubmission(self.submission_directory_name, expected_file.strip(".cpp").strip(".h"))

            # Ensures files exist
            if (not submission_file_name):
                found_all_files = False
                self.make_deduction(100, "Could not locate your .cpp file. Ensure your file is correctly named and zipped.")
                continue
            else:
                # Set location of files
                self.assignment_names.append(submission_file_name)

                submission_file_path = self.submission_directory_name + "/" + submission_file_name
                self.location_of_files.append(submission_file_path)


        return found_all_files



    def compile(self, submission_file, compiled_program_name):
        return CPPCompiler.compileCPPFile(submission_file, compiled_program_name, "Assignment File")


    def check_compile(self):

        # Iterate through submission files (if numerous .cpp in .zip file)
        for submission_file, assignment_name in zip(self.location_of_files, self.assignment_names):

            compiled_program_name = submission_file.replace(".cpp", "")
            program_compiles = self.compile(submission_file, compiled_program_name)

            if not program_compiles:
                self.make_deduction(100, "{} does not compile. Check your coding with c++11 standard.".format(assignment_name))
                return False

        return True







    def generate_test_data(self):
        """
            EDIT THIS FUNCTION PER ASSIGNMENT -- TEST CASES GO HERE
        """
        self.test_data = {}
        # Output

        out1 = "Hello, CS1300 World!"

        self.test_output = [out1]


    def test_cases(self, helper_path):

        points_lost = []
        expected_outputs = self.test_output

        # Starts process
        filename_to_process = self.location_of_files[0].replace(".cpp", "")

        process = subprocess.Popen(filename_to_process, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=sys.stderr, shell=True)

        # Sending inputs and receiving outputs and errs
        out, err = process.communicate(input=None, timeout=10) # Pass inputs and receive outputs and errs

        student_answers = out.decode().split("\n")                                           # Splits the console output by newline character into a list of all outputs

        # Clean student answers from empty newlines at very end of program; e.g., very last cout has endl; this is fine!
        if student_answers[-1] == '':
            student_answers = student_answers[:-1]


        # Check for correct answers
        num_student = len(student_answers)
        num_expected = len(expected_outputs)

        if num_student == 0:

            points_lost.append([100, "Your file gives no output! Ensure you are using cout rather than return."])


        elif num_student > num_expected:
            lost_point = 20
            points_lost.append([lost_point, "Incorrect number of outputs. Your file should cout {} outputs. Check for correct formatting of output string!".format(num_expected)])

        if num_student:
            function_num = 0
            for index, (expected_answer, student_answer) in enumerate(zip(expected_outputs, student_answers)):
                if index == 0:
                    index = 1
                if index % 2 == 0:
                    function_num += 1

                expected = expected_answer.replace(" ", "").lower()
                student = student_answer.replace(" ", "").lower()
                studentFeedback("{:6s}{:40s}{:10s}{:40s}".format("", "Expected Output", "", "Your Ouput"))
                studentFeedback("{:6s}{:40s}{:10s}{:40s}".format("", "---------------", "", "----------"))
                if expected != student:
                    studentFeedback("{:4s}{:2s}{:40s}{:10s}{:40s}{:2s}".format("", "**", expected_answer, "", student_answer, "**"))
                    points_lost.append([50, "Incorrect Answer. Expected Output: {} {:4} Your Output: {}".format(expected_answer, "", student_answer)])
                else:
                    studentFeedback("{:6s}{:40s}{:10s}{:40s}{:2s}".format("", expected_answer, "", student_answer, ""))
                studentFeedback("\n")


        for point_lost in points_lost:
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

        grade = 100                                             # Set max grade
        comments = ""                                           # Initialize comments string

        # Iterate through deductions list and decrement grade and append respective comment to comments string.
        for gradeDeduction, comment in self.deductions:
            grade += gradeDeduction
            comments += ("[%.1f] " % gradeDeduction) + comment + "\n"

        # Case: Student has 100%
        if (len(self.deductions)==0):
            comments = "Great work!"

        # Case: Less than 100%. Prints comments to student for suggestions on improvement.
        else:
            comments = comments.strip("\r").strip("\n")

        self.comments = comments            # Stores comments to object
        self.grade = max(round(grade),0)    # Stores grade to object


    def give_feedback(self):
        """
            Sends comments to studentFeedback object for report.
        """
        studentFeedback(self.comments)


    def print_grade(self):
        """
            Prints the final grade to stdout
        """
        sys.stderr.write("__________________________\n")
        sys.stderr.write("Score ---------------> {:2d}\n".format(self.grade))

        print(self.grade)

def main(argv):
    """
        MAIN function.
    """

    #Assign all output to the stderr stream as a catch all
    stdoutStream = sys.stdout
    sys.stdout = sys.stderr

    sub_dir = os.path.abspath(argv[0])
    tst_dir = os.path.abspath(argv[1])

    if not os.path.exists(sub_dir):
        sys.stderr.write("Could not find submission directory: '{:s}'\n".format(sub_dir))
        #return -1

    if not os.path.exists(tst_dir):
        sys.stderr.write("Could not find test directory: '{:s}'\n".format(tst_dir))


    submission = GradeSubmission(sub_dir, tst_dir)                 # Instantiate and construct grading object
    submission.grade_and_comment()                                 # Grade and generate comments for the assignment
    submission.give_feedback()                                     # Provide student feedback
    sys.stdout = stdoutStream
    submission.print_grade()                                       # Provide student final grade




if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
