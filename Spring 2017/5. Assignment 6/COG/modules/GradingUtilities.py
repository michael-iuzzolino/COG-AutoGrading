import sys
import subprocess, sys
import numpy as np


def studentFeedback(*strToPrint, new_line=True):
    if new_line:
        print(*strToPrint,file=sys.stderr)
    else:
        print(*strToPrint,file=sys.stderr, end="")


def compileCPPFile(sourceFileName, outputFileName):
    try:
        call_ = "g++ " + sourceFileName + " -o " + outputFileName + " -std=c++11"
        subprocess.check_call(call_,stdout=sys.stderr,stderr=sys.stderr,shell=True)
        return True

    except Exception:
        return False
