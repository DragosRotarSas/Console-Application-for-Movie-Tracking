import os

import logic
import repo

# ========
# LOGIC.PY
# ========

def test_add_user():
    users = []
    logic.add_user(users, "User1", 19)
    assert len(users) == 1
    assert users[0] == {"name": "User1", "age": 19}

def test_delete_user():
    users = [{"name": "User1", "age": 19}, {"name": "User2", "age": 19}]
    logic.delete_user(users, 0)
    assert len(users) == 1
    assert users[0]["name"] == "User2"

def test_update_user():
    users = [{"name": "User1", "age": 19}]
    logic.update_user(users, 0, "User1 Lastname", 21)
    assert users[0] == {"name": "User1 Lastname", "age": 21}

def test_is_valid_date():
    assert logic.is_valid_date("15.08.2023") == True
    assert logic.is_valid_date("31.12.1999") == True
    assert logic.is_valid_date("35.08.2023") == False
    assert logic.is_valid_date("2023-08-15") == False
    assert logic.is_valid_date("") == False

def test_add_movie():
    movies = []
    logic.add_movie(movies, "Inception", "16.07.2010", 8.8, ["Leonardo DiCaprio", "Tom Hardy"])
    assert len(movies) == 1
    assert movies[0]["name"] == "Inception"
    assert movies[0]["imdb_score"] == 8.8
    assert movies[0]["actors"] == ["Leonardo DiCaprio", "Tom Hardy"]

def test_delete_movie():
    movies = [
        {"name": "Inception", "release_date": "01.01.2010", "imdb_score": 8.8, "actors": ["DiCaprio"]},
        {"name": "Matrix", "release_date": "01.01.1999", "imdb_score": 8.7, "actors": ["Keanu Reeves"]}
    ]
    logic.delete_movie(movies, 0)
    assert len(movies) == 1
    assert movies[0]["name"] == "Matrix"

def test_update_movie_imdb():
    movies = [{"name": "Inception", "release_date": "01.01.2010", "imdb_score": 8.8, "actors": ["DiCaprio"]}]
    logic.update_movie_imdb(movies, 0, 9.2)
    assert movies[0]["imdb_score"] == 9.2

def test_add_watch_entry():
    watchlists = []
    logic.add_watch_entry(watchlists, "User1", "Inception")
    assert len(watchlists) == 1
    assert watchlists[0] == {"user_name": "User1", "movie_name": "Inception"}

def test_check_if_user_exists():
    users = [{"name": "User1", "age": 19}]
    assert logic.check_if_user_exists(users, "User1") == True
    assert logic.check_if_user_exists(users, "User2") == False
    assert logic.check_if_user_exists([], "User1") == False

def test_check_if_movie_exists():
    movies = [{"name": "Inception", "release_date": "01.01.2010", "imdb_score": 8.8, "actors": []}]
    assert logic.check_if_movie_exists(movies, "Inception") == True
    assert logic.check_if_movie_exists(movies, "American Psycho") == False

def test_get_movies_watched_by_user():
    watchlists = [
        {"user_name": "User1", "movie_name": "Inception"},
        {"user_name": "User2", "movie_name": "Seven"},
        {"user_name": "User1", "movie_name": "Interstellar"}
    ]
    assert logic.get_movies_watched_by_user(watchlists, "User1") == ["Inception", "Interstellar"]
    assert logic.get_movies_watched_by_user(watchlists, "Bogdan") == []

def test_get_movies_with_actor():
    movies = [
        {"name": "Inception", "release_date": "01.01.2010", "imdb_score": 8.8, "actors": ["Leonardo DiCaprio", "Tom Hardy"]},
        {"name": "Seven", "release_date": "01.01.1995", "imdb_score": 8.6, "actors": ["Brad Pitt"]}
    ]
    result = logic.get_movies_with_actor(movies, "leonardo dicaprio")
    assert len(result) == 1
    assert result[0]["name"] == "Inception"
    assert logic.get_movies_with_actor(movies, "Tom Holland") == []

def test_get_movies_with_rating():
    movies = [
        {"name": "Inception", "release_date": "01.01.2010", "imdb_score": 8.8, "actors": []},
        {"name": "Seven", "release_date": "01.01.1995", "imdb_score": 8.6, "actors": []}
    ]
    result = logic.get_movies_with_rating(movies, 8.8)
    assert len(result) == 1
    assert result[0]["name"] == "Inception"
    assert len(logic.get_movies_with_rating(movies, 9.5)) == 0

def test_get_sorted_watchlists():
    watchlists = [
        {"user_name": "User2", "movie_name": "Matrix"},
        {"user_name": "User1", "movie_name": "Inception"}
    ]
    sorted_list = logic.get_sorted_watchlists(watchlists)
    assert sorted_list[0]["user_name"] == "User1"
    assert sorted_list[1]["user_name"] == "User2"

# =======
# REPO.PY
# =======

def test_save_and_read_users():
    test_path = "test_users.txt"
    users = [{"name": "User1", "age": 19}, {"name": "User2", "age": 19}]
    repo.save_users(test_path, users)
    assert repo.read_users(test_path) == users
    os.remove(test_path)
    assert repo.read_users("fisier_inexistent.txt") == []

def test_save_and_read_movies():
    test_path = "test_movies.txt"
    movies = [
        {"name": "Inception", "release_date": "01.01.2010", "imdb_score": 8.8, "actors": ["Leonardo DiCaprio", "Tom Hardy"]}
    ]
    repo.save_movies(test_path, movies)
    assert repo.read_movies(test_path) == movies
    os.remove(test_path)
    assert repo.read_movies("fisier_inexistent.txt") == []

def test_save_and_read_watch():
    test_path = "test_watch.txt"
    watchlists = [{"user_name": "User1", "movie_name": "Inception"}]
    repo.save_watch(test_path, watchlists)
    assert repo.read_watch(test_path) == watchlists
    os.remove(test_path)
    assert repo.read_watch("fisier_inexistent.txt") == []


def run_all_tests():
    test_add_user()
    test_delete_user()
    test_update_user()
    test_is_valid_date()
    test_add_movie()
    test_delete_movie()
    test_update_movie_imdb()
    test_add_watch_entry()
    test_check_if_user_exists()
    test_check_if_movie_exists()
    test_get_movies_watched_by_user()
    test_get_movies_with_actor()
    test_get_movies_with_rating()
    test_get_sorted_watchlists()
    test_save_and_read_users()
    test_save_and_read_movies()
    test_save_and_read_watch()
    print("All tests passed.")

if __name__ == "__main__":
    run_all_tests()