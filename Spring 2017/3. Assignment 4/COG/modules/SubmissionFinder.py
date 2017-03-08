import os, sys

class SubmissionFinder:

    def __init__(self, acceptableExtensions = [".cpp",".cc",".c++"]):
        self.acceptableExtensions = acceptableExtensions

    def validateFileName(self, expectedFileName, actualFileName):
        """
        Checks the following conditions:
            1. The actual file name must be => than expected file name in length
                    We expect the student file names to be:         lastname_firstname_assignment#.cpp
                    We are testing against expected files such as:  assignment1.cpp

            2. The expected file name must be in the actual file name
                    e.g., "assignment1" is in "iuzzolino_michael_assignment1"; therefore, evaluate as true

                    Note:
                    if len(expectedFileName) > len(actualFileName), then condition 2 would fail by default

            3. Actual file name must acceptable extensions, as defined in the class constructor

            4. File cannot be a hidden ('.') or backup ('~') file.
        """

        # Condition 1
        if (len(actualFileName) < len(expectedFileName)):
            return False

        # Condition 2
        containsText = expectedFileName.lower() in actualFileName.lower()   # "a in b" returns True or False

        # Condition 3
        hasCorrectExtension = False                                         # Sets correct extension FLAG as false
        for extension in self.acceptableExtensions:                         # Iterate through extensions in acceptable Extensions defined in constructor
            if (extension.lower() in actualFileName.lower()):               # Evaluates whether current extension is in actual file name
                hasCorrectExtension = True
                break                                                       # Match found. Can break for loop.

        # Condition 4
        isNotHiddenOrBackupFile = actualFileName[0] != '.' and actualFileName[0] != '~'

        # Evaluate if file is acceptable
        fileIsAcceptable = containsText and hasCorrectExtension and isNotHiddenOrBackupFile

        return fileIsAcceptable



    def findSubmission(self, submissionDirectory, expectedFileName):
        """
        Tries to locate the student's file within the directory of submitted files

        """
        try:
            submissionFiles = os.listdir(submissionDirectory)             # Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order. It does not include the special entries '.' and '..' even if they are present in the directory.
            #print("\n\tFiles: {}".format(submissionFiles))

            #print("\n\tIterating through files in directory...")
            for submissionFile in submissionFiles:
                #print("\t\tFile: {}".format(submissionFile))
                if (self.validateFileName(expectedFileName, submissionFile)):
                    return submissionFile
            return False

        except Exception as e:
            print ("Error when looking for submission similar to " + expectedFileName + "...\n", e.strerror, file = sys.stderr)
            return False
