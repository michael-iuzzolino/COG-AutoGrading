import subprocess
import sys
import os

def compileCPPFile(sourceFileName, outputFileName, displayName):
    """
    try:
        print("--------------Compiling " + displayName + " source code--------------",file=sys.stderr)
        subprocess.check_call("g++ \""+sourceFileName+"\" -std=c++11 -o \"" + outputFileName + "\"",stdout=sys.stderr,stderr=sys.stderr,shell=True) 
        return True
    """
    #print("\n\n\tCOMPILING...")
    #print("\t------------------------------------------------------------------")
    #print("\t\tsourceFileName: {}".format(sourceFileName))
    #print("\t\toutputFileName: {}".format(outputFileName))
    #print("\t\tdisplayName: {}".format(displayName))
    
    #os.system('pwd')
    
    #print("process call: g++ \"" + sourceFileName + "\" -std=c++11 -o \"" + outputFileName + "\"")
    #print("\t------------------------------------------------------------------")
    #print("\n\n")
    try:
        print("--------------Compiling " + displayName + " source code--------------",file=sys.stderr)
        subprocess.check_call("g++ \""+sourceFileName+"\" -std=c++11 -o \"" + outputFileName + "\"",stdout=sys.stderr,stderr=sys.stderr,shell=True) 
        return True

    except Exception:
        print("-------------ERROR WHILE COMPILING!------------",file=sys.stderr)
        return False