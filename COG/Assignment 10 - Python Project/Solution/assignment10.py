import numpy as np
import os

class Recommender(object):
    def __init__(self, books_filename, ratings_filename):
        print(os.getcwd())
        self.books_dict = self.read_books(books_filename)
        self.ratings_dict = self.read_users(ratings_filename)
        self.calculate_average_rating()


    def read_books(self, file_name):
        """
        """
        try:
            with open(file_name, "r") as infile:
                return { index : line.strip().split(",")[::-1] for index, line in enumerate(infile) }

        except:
            return None


    def read_users(self, file_name):
        """
        """
        try:
            ratings_dict = {}
            with open(file_name, "r") as infile:
                for line in infile:
                    line = line.strip()
                    if len(line) == 0:
                        continue

                    line_list = line.split(" ")
                    user_name = line_list[0]
                    ratings = list(int(rating) for rating in line_list[1:])
                    ratings_dict[user_name] = ratings

            return ratings_dict

        except:
            return None


    def calculate_average_rating(self):
        """
        """
        self.average_rating_dict = {}

        for book_index in self.books_dict.keys():
            rating_sum = 0.0
            rating_count = 0
            for user_rating in self.ratings_dict.values():
                rating_sum += user_rating[book_index]
                rating_count += 1 if user_rating[book_index] != 0 else 0

            self.average_rating_dict[book_index] = rating_sum / rating_count


    def lookup_average_rating(self, book_index):
        """
        """
        average_rating_string = ""

        # Get the average rating
        average_rating = self.average_rating_dict[book_index]

        # Get book title and author. Split on ,
        book_author_and_title = self.books_dict[book_index]

        book_title = book_author_and_title[0]
        book_author = book_author_and_title[1]

        average_rating_string = "({:0.2f}) {} by {}".format(average_rating, book_title, book_author)

        return average_rating_string


    def calc_similarity(self, user1, user2):
        """
        """
        user1_ratings = self.ratings_dict[user1]
        user2_ratings = self.ratings_dict[user2]
        similarity_measure = np.dot(user1_ratings, user2_ratings)

        return similarity_measure

    def get_most_similar_user(self, current_user_id):
        """
        """
        current_user_ratings = self.ratings_dict[current_user_id]

        best_similarity = 0
        best_user_match_id = None
        for other_user_id, other_user_ratings in self.ratings_dict.items():
            if current_user_id == other_user_id:
                continue

            similarity = self.calc_similarity(current_user_id, other_user_id)
            if similarity > best_similarity:
                best_similarity = similarity
                best_user_match_id = other_user_id

        return best_user_match_id


    def recommend_books(self, current_user_id):
        """
        """

        # Set list of match_ratings
        match_ratings = [3, 5]

        # First, we want to find the most similar user
        most_similar_user_id = self.get_most_similar_user(current_user_id)

        # We want their ratings, and find the book ids that are rated as 3 or 5
        most_similar_user_ratings = self.ratings_dict[most_similar_user_id]

        # Find current user's ratings.
        current_user_ratings = self.ratings_dict[current_user_id]

        recommendations_list = []
        for book_id, book_rating in enumerate(most_similar_user_ratings):
            if book_rating not in match_ratings:
                continue

            if current_user_ratings[book_id] != 0:
                continue

            # Compare similar user's 3 and 5 rated books to current user. Match if current user rating == 0
            new_book_recommendation = self.lookup_average_rating(book_id)

            # Append new book to recommendations list
            recommendations_list.append(new_book_recommendation)

        return recommendations_list




def main():
    books_filname = "books.txt"
    ratings_filname = "ratings.txt"

    recommender_system = Recommender(books_filname, ratings_filname)

    # Test system
    print(recommender_system.recommend_books("Ben"))


if __name__ == "__main__":
    main()
