import sys, os
import subprocess
import numpy as np


def studentFeedback(*strToPrint, new_line=True):
    if new_line:
        print(*strToPrint,file=sys.stderr)
    else:
        print(*strToPrint,file=sys.stderr, end="")


def compileCPPFile(sourceFileName, outputFileName):
    try:
        call_ = "g++ {} -o {} -std=c++11".format(sourceFileName, outputFileName)
        subprocess.check_call(call_, stdout=sys.stderr, stderr=sys.stderr, shell=True)
        return True

    except Exception:
        return False
