import numpy as np
import os
from modules.assignment10_solution import Recommender
import inspect

test_cases_list = [{"__init__" : {}},
                   {"read_books" : {}},
                   {"read_users" : {}},
                   {"calc_similarity" : {}},
                   {"get_most_similar_user" : {}},
                   {"recommend_books" : {}}
                  ]


def Constructor_TEST_GEN(test_num):
    # Set input
    test_cases_list[test_num]["__init__"]["input"] = test_num

    # define recommender object
    new_system = Recommender("files/books.txt", "files/ratings.txt")

    # Find number of attributes
    attributes = inspect.getmembers(new_system, lambda a:not(inspect.isroutine(a)))
    num_attributes = len([a[0] for a in attributes if '__' not in a[0]])

    # Set output
    test_cases_list[test_num]["__init__"]["output"] = [str(num_attributes)]


def read_books_TEST_GEN(test_num):

    # Set input
    test_cases_list[test_num]["read_books"]["input"] = test_num

    # define recommender object
    new_system = Recommender("files/books.txt", "files/ratings.txt")

    # First test case: return None with incorrect txt
    none_dict = new_system.read_books("fail.txt")

    # Second test case: return Good dict
    returned_dict = new_system.read_books("files/books.txt")

    # Append test cases to list
    test_cases_list[test_num]["read_books"]["output"] = [none_dict, returned_dict]

def read_users_TEST_GEN(test_num):

    # Set input
    test_cases_list[test_num]["read_users"]["input"] = test_num

    # define recommender object
    new_system = Recommender("files/books.txt", "files/ratings.txt")

    # First test case: return None with incorrect txt
    none_dict = new_system.read_users("fail.txt")

    # Second test case: return Good dict
    returned_dict = new_system.read_users("files/ratings.txt")

    # Append test cases to list
    test_cases_list[test_num]["read_users"]["output"] = [none_dict, returned_dict]



def calc_similarity_TEST_GEN(test_num):

    # Set input
    test_cases_list[test_num]["calc_similarity"]["input"] = test_num

    # define recommender object
    new_system = Recommender("files/books.txt", "files/ratings.txt")

    # First test case: pick 2 random users and check similarity
    user1 = "Albus_Dumbledore"
    user2 = "Harry_Potter"

    similarity_1 = str(new_system.calc_similarity(user1, user2))

    # Second test case: pick 2 random users and check similarity
    user1 = "YJAM"
    user2 = "Apollo"

    similarity_2 = str(new_system.calc_similarity(user1, user2))

    # Append test cases to list
    test_cases_list[test_num]["calc_similarity"]["output"] = [similarity_1, similarity_2]


def get_most_similar_user_TEST_GEN(test_num):

    # Set input
    test_cases_list[test_num]["get_most_similar_user"]["input"] = test_num

    # define recommender object
    new_system = Recommender("files/books.txt", "files/ratings.txt")

    # First test case: pick a random user and find the most similar user
    user1 = "Albus_Dumbledore"

    most_similar_1 = str(new_system.get_most_similar_user(user1))

    test_cases_list[test_num]["get_most_similar_user"]["output"] = [most_similar_1]
    # # Second test case: pick a random user and find the most similar user
    # user1 = "Harry_Potter"
    #
    # most_similar_2 = str(new_system.get_most_similar_user(user1))
    #
    # # Append test cases to list
    # test_cases_list[test_num]["get_most_similar_user"]["output"] = [most_similar_1, most_similar_2]
    #


def recommend_books_TEST_GEN(test_num):

    # Set input
    test_cases_list[test_num]["recommend_books"]["input"] = test_num

    # define recommender object
    new_system = Recommender("files/books.txt", "files/ratings.txt")

    # First test case: pick a random user and find the most similar user
    user1 = "Albus_Dumbledore"

    recommended_books_1 = str(new_system.recommend_books(user1))

    # Second test case: pick a random user and find the most similar user
    user2 = "NaRwHaLs"

    recommended_books_2 = str(new_system.recommend_books(user2))

    # Append test cases to list
    test_cases_list[test_num]["recommend_books"]["output"] = [recommended_books_1, recommended_books_2]




def generate_test_cases():

    TEST_GENS = [Constructor_TEST_GEN, read_books_TEST_GEN, read_users_TEST_GEN,
                 calc_similarity_TEST_GEN, get_most_similar_user_TEST_GEN, recommend_books_TEST_GEN]

    for test_num, test_gen_fxn in enumerate(TEST_GENS):
        test_gen_fxn(test_num)

    return test_cases_list
