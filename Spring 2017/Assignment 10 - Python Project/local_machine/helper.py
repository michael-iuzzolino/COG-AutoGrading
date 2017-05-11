
import numpy as np
import sys
import inspect

from assignment10_cleaned import *

def TEST_constructor():

    # Setup recommender object
    recommender_system = Recommender(io_default[0], io_default[1])

    # Find number of attributes
    attributes = inspect.getmembers(recommender_system, lambda a:not(inspect.isroutine(a)))
    num_attributes = len([a[0] for a in attributes if '__' not in a[0]])
    print(num_attributes)


def TEST_read_books():

    # Setup recommender object
    recommender_system = Recommender(io_default[0], io_default[1])

    # Test case 1: Fail read file - return None
    return_dict = recommender_system.read_books("fail.txt")
    print(return_dict)

    # Test case 2: Succesful read file
    return_dict = recommender_system.read_books(io_default[0])
    print(return_dict)

def TEST_read_users():

    # Setup recommender object
    recommender_system = Recommender(io_default[0], io_default[1])

    # Test case 1: Fail read file - return None
    return_dict = recommender_system.read_users("fail.txt")
    print(return_dict)

    # Test case 2: Succesful read file
    return_dict = recommender_system.read_users(io_default[1])
    print(return_dict)



def TEST_calc_similarity():
    # Setup recommender object
    recommender_system = Recommender(io_default[0], io_default[1])

    # Test case 1: pick 2 users at "random" and get similarity
    user1 = "Albus_Dumbledore"
    user2 = "Harry_Potter"

    similarity_1 = str(recommender_system.calc_similarity(user1, user2))
    print(similarity_1)

    # Test case 2: pick 2 users at "random" and get similarity
    user1 = "YJAM"
    user2 = "Apollo"

    similarity_2 = str(recommender_system.calc_similarity(user1, user2))
    print(similarity_2)




def TEST_get_most_similar_user():
    # Setup recommender object
    recommender_system = Recommender(io_default[0], io_default[1])

    # Test case 1: pick 2 users at "random" and get similarity
    user1 = "Albus_Dumbledore"

    most_similar_1 = recommender_system.get_most_similar_user(user1)
    print(most_similar_1)

    # # Test case 2: pick 2 users at "random" and get similarity
    # user2 = "Harry_Potter"
    #
    # most_similar_2 = recommender_system.get_most_similar_user(user2)
    # print(most_similar_2)



def TEST_recommend_books():
    # Setup recommender object
    recommender_system = Recommender(io_default[0], io_default[1])

    # Test case 1: pick 2 users at "random" and get similarity
    user1 = "Albus_Dumbledore"

    recommended_books_1 = recommender_system.recommend_books(user1)
    print(recommended_books_1)

    # Test case 2: pick 2 users at "random" and get similarity
    user2 = "NaRwHaLs"

    recommended_books_2 = recommender_system.recommend_books(user2)
    print(recommended_books_2)


def main(cmd_line_arguments):

    global io_default
    io_default = [cmd_line_arguments[1], cmd_line_arguments[2]]


    test_case_map = [TEST_constructor, TEST_read_books, TEST_read_users,
                     TEST_calc_similarity, TEST_get_most_similar_user, TEST_recommend_books]


    # Test system
    test_number = int(input())

    # Run test case
    test_case_map[test_number]()




if __name__ == "__main__":
    main(sys.argv)
