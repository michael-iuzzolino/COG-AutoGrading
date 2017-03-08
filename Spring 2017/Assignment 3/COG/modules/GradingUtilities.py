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

    test_input = []
    test_output = []


    # Problem 1
    plural_nouns = ["lettuce", "toasters", "psychics", "ponies", "ninjas"]
    singular_nouns = ["squirrel", "commonomer", "cold", "criminal"]
    occupations = ["teen-exorcist", "shredded-cheese-authority", "cat-behavior-consultant", "dittybopper"]
    animal_names = ["lyger", "trash-panda", "fart-squirrel", "lemur", "human", "sloth"]
    places = ["Seoul", "Bergen", "Osaka", "Beijing", "Kathmandu"]
    verbs = ["poke", "twerk", "hug", "devour", "smack"]

    # Testcases 1 - 3
    for i in range(3):
        # Testcase 1
        plural_noun = plural_nouns[np.random.randint(len(plural_nouns))]         # Plural Noun
        singular_noun = singular_nouns[np.random.randint(len(singular_nouns))]         # Singular Noun
        occupation = occupations[np.random.randint(len(occupations))]         # Occupation
        animal_name = animal_names[np.random.randint(len(animal_names))]         # Animal Name
        place = places[np.random.randint(len(places))]         # Place
        verb = verbs[np.random.randint(len(verbs))]        # Verb
        test_input.append(plural_noun)
        test_input.append(singular_noun)
        test_input.append(occupation)
        test_input.append(animal_name)
        test_input.append(place)
        test_input.append(verb)


        mad_lib = "In the book War of the {0}, the main character is an anonymous {1}" \
                  " who records the arrival of the {2}s in {3} -- Needless to say, havoc reigns as the {2}s" \
                  " continue to {4} everything in sight, " \
                  "until they are killed by the common {5}." \
                  .format(plural_noun, occupation, animal_name, place, verb, singular_noun)
        test_output.append([mad_lib])


    # Problem 2
    # Testcases 1-3 for energyCalculator
    out1 = "The average annual solar energy production is 2812.5 kWh."
    out2 = "The average annual solar energy production is 8100 kWh."
    out3 = "The average annual solar energy production is 10980 kWh."

    # Testcases 4-9 for printEnergy
    out4 = "The average annual solar energy for an efficiency of 0.1 is 1875 kWh."
    out5 = "The average annual solar energy for an efficiency of 0.15 is 2812.5 kWh."
    out6 = "The average annual solar energy for an efficiency of 0.2 is 3750 kWh."
    out7 = "The average annual solar energy for an efficiency of 0.25 is 4687.5 kWh."
    out8 = "The average annual solar energy for an efficiency of 0.3 is 5625 kWh."
    out9 = "The average annual solar energy for an efficiency of 0.35 is 6562.5 kWh."


    # Testcases 10-12 for calculateNumberHousesSupported
    out10 = "3 houses can be supported."
    out11 = "0 houses can be supported."
    out12 = "55 houses can be supported."
    test_output.append([out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12])

    flattened_list = [y for x in test_output for y in x]
    test_output = flattened_list

    return test_input, test_output
