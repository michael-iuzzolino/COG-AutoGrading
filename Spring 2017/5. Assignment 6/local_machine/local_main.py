#!/usr/bin/env python3

"""
Author: Michael Louis Iuzzolino
Institution: University of Colorado Boulder
"""

#CSCI 1300 - Assignment 2 Grader
#THESE LINES ARE NEEDED TO ADD THE GradingScriptLibrary path to the system path so they can be imported!!!
import os,sys,inspect
import re


cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../../../")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
#DO NOT DELETE THE LINES ABOVE


anyNumberRE =  re.compile("([-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?)")

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
