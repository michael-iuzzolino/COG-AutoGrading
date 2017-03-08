import sys
import subprocess, sys
import numpy as np


def studentFeedback(*strToPrint, new_line=True):
    if new_line:
        print(*strToPrint,file=sys.stderr)
    else:
        print(*strToPrint,file=sys.stderr, end="")


def compileCPPFile(sourceFileName, outputFileName, displayName):
    try:
        subprocess.check_call("g++ \""+sourceFileName+"\" -std=c++11 -o \"" + outputFileName + "\"",stdout=sys.stderr,stderr=sys.stderr,shell=True)
        return True

    except Exception:
        return False


def generateTestData():
    """
        EDIT THIS FUNCTION PER ASSIGNMENT -- TEST CASES GO HERE
    """
    # Output

    out1 = "The population is 331510200."
    out2 = "The time is 0 hours, 0 minutes, and 0 seconds."
    out3 = "The time is 24 hours, 0 minutes, and 0 seconds."
    out4 = "0 degrees Celsius is 32 degrees Fahrenheit."
    out5 = "100 degrees Celsius is 212 degrees Fahrenheit."

    test_output = [out1, out2, out3, out4, out5]


    # Input
    in1 = "0"
    in2 = "86400"
    in3 = "0"
    in4 = "100"
    test_input = [in1, in2, in3, in4]

    return test_input, test_output
