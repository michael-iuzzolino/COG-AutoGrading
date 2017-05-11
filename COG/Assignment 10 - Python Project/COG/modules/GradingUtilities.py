import sys, os
import subprocess
import numpy as np
import time
# from termcolor import colored


def studentFeedback(*strToPrint, new_line=True, end_char=""):
    if new_line:
        print(*strToPrint,file=sys.stderr)
    else:
        print(*strToPrint,file=sys.stderr, end=end_char)


def compileCPPFile(sourceFileName, outputFileName):
    try:
        call_ = "g++ {} -o {} -std=c++11".format(sourceFileName, outputFileName)
        subprocess.check_call(call_, stdout=sys.stderr, stderr=sys.stderr, shell=True)
        return True

    except Exception:
        return False


def progress_update(time_step=0.02):
    print("\t\tProgress")
    for i in range(0,21):
        print("\r\t\t[{:21s}] \t {:2.0f}%".format("="*i+"*", i/21*100), end="")
        time.sleep(time_step)

    # text = colored('100%', 'green', attrs=['underline', 'bold'])
    text = "100%"
    print("\r\t\t[{:21s}] \t {}".format("="*(i+1), text), end="")
    print("\n")
