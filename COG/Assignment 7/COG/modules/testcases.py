import numpy as np

def generate_test_cases():
    test_case_num_to_description = {"SpellChecker" : {}, "WordCounts" : {} }

    test_case_dict = {"SpellChecker" : {}, "WordCounts" : {} }
    input_print_dictionary = {}

    number_test_cases = 6;

    # SpellChecker Tests
    # Test case 0
    testcase_input_0 = ["0"]
    testcase_output_0 = []
    test_case_dict["SpellChecker"][0] = {"input" : testcase_input_0, "output" : testcase_output_0}
    test_case_num_to_description["SpellChecker"][0] = "Default Constructor"


    # Test case 1
    testcase_input_1 = ["1"]
    testcase_output_1 = ["Begin marker: [", "End marker: ]", "Begin marker: *", "End marker: @"]
    test_case_dict["SpellChecker"][1] = {"input" : testcase_input_1, "output" : testcase_output_1}
    test_case_num_to_description["SpellChecker"][1] = "Set and Get Begin/Ending Markers"


    # Test case 2
    testcase_input_2 = ["2"]
    testcase_output_2 = ["Language: American", "Begin marker: [", "End marker: ]"]
    test_case_dict["SpellChecker"][2] = {"input" : testcase_input_2, "output" : testcase_output_2}
    test_case_num_to_description["SpellChecker"][2] = "Single Parameter Constructor"


    # Test case 3
    testcase_input_3 = ["3", "VALID_WORDS_3000.txt", "MISSPELLED.txt"]
    testcase_output_3 = ["Language: English"]
    test_case_dict["SpellChecker"][3] = {"input" : testcase_input_3, "output" : testcase_output_3}
    test_case_num_to_description["SpellChecker"][3] = "Three Parameter Constructor"

    # Test case 4
    testcase_input_4 = ["4"]
    testcase_output_4 = ["Correctly loaded: 0", "Fixed string: [today]", "Correctly loaded: 1", "Correctly loaded: 1", "Fixed string: today"]
    test_case_dict["SpellChecker"][4] = {"input" : testcase_input_4, "output" : testcase_output_4}
    test_case_num_to_description["SpellChecker"][4] = "loadValidWords method"

    # Test case 5
    testcase_input_5 = ["5"]
    testcase_output_5 = ["Correctly loaded: 0", "Correctly loaded: 1", "Correctly loaded: 1", "Fixed string: today"]
    test_case_dict["SpellChecker"][5] = {"input" : testcase_input_5, "output" : testcase_output_5}
    test_case_num_to_description["SpellChecker"][5] = "loadMisspelledWords method"

    # Test case 6
    testcase_input_6 = ["6"]
    testcase_output_6 = ["Fixed string: today", "Fixed string: cake", "Fixed string: climb"]
    test_case_dict["SpellChecker"][6] = {"input" : testcase_input_6, "output" : testcase_output_6}
    test_case_num_to_description["SpellChecker"][6] = "fixUp method - Single word: correct"

    # Test case 7
    testcase_input_7 = ["7"]
    testcase_output_7 = ["Fixed string: today", "Fixed string: banner", "Fixed string: hater"]
    test_case_dict["SpellChecker"][7] = {"input" : testcase_input_7, "output" : testcase_output_7}
    test_case_num_to_description["SpellChecker"][7] = "fixUp method - Single word: misspelled"


    # Test case 8
    testcase_input_8 = ["8"]
    testcase_output_8 = ["Fixed string: *toodayy*", "Fixed string: *hmewrkk*", "Fixed string: *instulatikon*"]
    test_case_dict["SpellChecker"][8] = {"input" : testcase_input_8, "output" : testcase_output_8}
    test_case_num_to_description["SpellChecker"][8] = "fixUp method - Single word: unknown"


    # Test case 9
    testcase_input_9 = ["9"]
    testcase_output_9 = ["Fixed string: about clock today", "Fixed string: clearly today intelligent", "Fixed string: necessary clock today"]
    test_case_dict["SpellChecker"][9] = {"input" : testcase_input_9, "output" : testcase_output_9}
    test_case_num_to_description["SpellChecker"][9] = "fixUp method - Multiword replacement of misspelled words"


    # Test case 10
    testcase_input_10 = ["10"]
    testcase_output_10 = ["Fixed string: today", "Fixed string: today", "Fixed string: today"]
    test_case_dict["SpellChecker"][10] = {"input" : testcase_input_10, "output" : testcase_output_10}
    test_case_num_to_description["SpellChecker"][10] = "fixUp method - Single words with punctuation: correct"


    # Test case 11
    testcase_input_11 = ["11"]
    testcase_output_11 = ["Fixed string: today", "Fixed string: today", "Fixed string: today"]
    test_case_dict["SpellChecker"][11] = {"input" : testcase_input_11, "output" : testcase_output_11}
    test_case_num_to_description["SpellChecker"][11] = "fixUp method - Single words with punctuation: misspelled"

    # Test case 12
    testcase_input_12 = ["12"]
    testcase_output_12 = ["Fixed string: *toodayy*", "Fixed string: *toodayy*", "Fixed string: *toodayy*"]
    test_case_dict["SpellChecker"][12] = {"input" : testcase_input_12, "output" : testcase_output_12}
    test_case_num_to_description["SpellChecker"][12] = "fixUp method - Single words with punctuation: unknown"



    # Test case 13
    testcase_input_13 = ["13", "VALID_WORDS_3000.txt", "MISSPELLED.txt"]
    testcase_output_13 = ["Fixed string: hello world", "Fixed string: comedy world", "Fixed string: hello emotional"]
    test_case_dict["SpellChecker"][13] = {"input" : testcase_input_13, "output" : testcase_output_13}
    test_case_num_to_description["SpellChecker"][13] = "fixUp method - Sentences: All correct"

    # Test case 14
    testcase_input_14 = ["14"]
    testcase_output_14 = ["Fixed string: hello today", "Fixed string: mosaic world", "Fixed string: hello neighbor"]
    test_case_dict["SpellChecker"][14] = {"input" : testcase_input_14, "output" : testcase_output_14}
    test_case_num_to_description["SpellChecker"][14] = "fixUp method - Sentences: One misspelled"

    # Test case 15
    testcase_input_15 = ["15"]
    testcase_output_15 = ["Fixed string: about today", "Fixed string: permissible about today phone", "Fixed string: about phonetic today"]
    test_case_dict["SpellChecker"][15] = {"input" : testcase_input_15, "output" : testcase_output_15}
    test_case_num_to_description["SpellChecker"][15] = "fixUp method - Sentences: All misspelled"

    # Test case 16
    testcase_input_16 = ["16"]
    testcase_output_16 = ["Fixed string: *abouuy* *toodayy*", "Fixed string: *permisssable* *abbouy* *toddayy* *foone*", "Fixed string: *hielo* *thiiis* *inini* *pudabi*"]
    test_case_dict["SpellChecker"][16] = {"input" : testcase_input_16, "output" : testcase_output_16}
    test_case_num_to_description["SpellChecker"][16] = "fixUp method - Sentences: All unknown"

    # Test case 17
    testcase_input_17 = ["17"]
    testcase_output_17 = ["Fixed string: today", "Fixed string: hello"]
    test_case_dict["SpellChecker"][17] = {"input" : testcase_input_17, "output" : testcase_output_17}
    test_case_num_to_description["SpellChecker"][17] = "fixUp method - Sentences: Multi-case words"


    # Test case 18
    testcase_input_18 = ["18"]
    testcase_output_18 = ["Fixed string: *tod!ay*", "Fixed string: *t?od!ay*", "Fixed string: *t?oday*"]
    test_case_dict["SpellChecker"][18] = {"input" : testcase_input_18, "output" : testcase_output_18}
    test_case_num_to_description["SpellChecker"][18] = "fixUp method - Sentences: Punctuation in words"



    # WordCounts Tests
    # Test case 1
    testcase_input_1 = ["1"]
    testcase_output_1 = []
    test_case_dict["WordCounts"][1] = {"input" : testcase_input_1, "output" : testcase_output_1}
    test_case_num_to_description["WordCounts"][1] = "Default Constructor"

    # WordCounts Tests
    # Test case 1
    testcase_input_1 = ["1"]
    testcase_output_1 = ["Count: 0", "Most common: 0"]
    test_case_dict["WordCounts"][1] = {"input" : testcase_input_1, "output" : testcase_output_1}
    test_case_num_to_description["WordCounts"][1] = "mostCommon"

    # Test case 2
    testcase_input_2 = ["2"]
    testcase_output_2 = ["Count: 1", "Count: 1", "Count: 1"]
    test_case_dict["WordCounts"][2] = {"input" : testcase_input_2, "output" : testcase_output_2}
    test_case_num_to_description["WordCounts"][2] = "countWords: Single word sentence"


    # Test case 3
    testcase_input_3 = ["3"]
    testcase_output_3 = ["Count: 1", "Count: 1", "Count: 1"]
    test_case_dict["WordCounts"][3] = {"input" : testcase_input_3, "output" : testcase_output_3}
    test_case_num_to_description["WordCounts"][3] = "countWords: Single word sentence with punctuation"

    # Test case 4
    testcase_input_4 = ["4"]
    testcase_output_4 = ["Count: 1"]
    test_case_dict["WordCounts"][4] = {"input" : testcase_input_4, "output" : testcase_output_4}
    test_case_num_to_description["WordCounts"][4] = "countWords: Single word sentence with mixed case"

    # Test case 5
    repeat1 = str(np.random.randint(2, 8))
    repeat2 = str(np.random.randint(2, 8))
    repeat3 = str(np.random.randint(2, 8))
    testcase_input_5 = ["5", repeat1, repeat2, repeat3]
    testcase_output_5 = ["Count: {}".format(repeat1), "Count: {}".format(repeat2), "Count: {}".format(repeat3)]
    test_case_dict["WordCounts"][5] = {"input" : testcase_input_5, "output" : testcase_output_5}
    test_case_num_to_description["WordCounts"][5] = "countWords: Same single word sentence"

    # Test case 6
    testcase_input_6 = ["6"]
    testcase_output_6 = ["Count: 1", "Count: 1", "Count: 1", "Count: 3"]
    test_case_dict["WordCounts"][6] = {"input" : testcase_input_6, "output" : testcase_output_6}
    test_case_num_to_description["WordCounts"][6] = "countWords: Multi-word sentences"

    # Test case 7
    testcase_input_7 = ["7"]
    testcase_output_7 = ["Count: 1", "Count: 1"]
    test_case_dict["WordCounts"][7] = {"input" : testcase_input_7, "output" : testcase_output_7}
    test_case_num_to_description["WordCounts"][7] = "countWords: Multi-word, sentences with punctuation"

    # Test case 8
    testcase_input_8 = ["8"]
    testcase_output_8 = ["Count: 1", "Count: 1"]
    test_case_dict["WordCounts"][8] = {"input" : testcase_input_8, "output" : testcase_output_8}
    test_case_num_to_description["WordCounts"][8] = "countWords: Multi-word,sentences with mixed case"

    return test_case_dict, test_case_num_to_description
