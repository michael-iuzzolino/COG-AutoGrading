#!/usr/bin/env python3
"""
Author: Michael Louis Iuzzolino
Institution: University of Colorado Boulder

Course: CSCI 1300 - Spring 2017
"""

import os,sys,inspect
import re

from cog_main import *

def local_main(argv):
    """
        Local main function.
    """

    student_submission_directory = os.path.abspath(argv[0])
    try:
        COG_script_directory = os.path.abspath(argv[1])
    except:
        COG_script_directory = os.getcwd()

    submission = GradeSubmission(student_submission_directory, COG_script_directory, local_test=True)                 # Instantiate and construct grading object
    submission.grade_and_comment()                                 # Grade and generate comments for the assignment
    submission.give_feedback()                                     # Provide student feedback
    submission.print_grade()                                       # Provide student final grade


if __name__ == "__main__":
    sys.exit(local_main(sys.argv[1:]))
