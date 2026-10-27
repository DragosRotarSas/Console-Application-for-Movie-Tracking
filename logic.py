import re

def add_user(users, name, age):
    new_user = {
        "name": name,
        "age": age
    }
    users.append(new_user)

def delete_user(users, user_id):
    del users[user_id]

def update_user(users, user_id, name, age):
    new_user = {
        "name": name,
        "age": age
    }
    users[user_id] = new_user

def is_valid_date(release_date):
    pattern = r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$"
    return bool(re.match(pattern, release_date))

def add_movie(movies, name, release_date, imdb_score, actors):
    new_movie = {
        "name": name,
        "release_date": release_date,
        "imdb_score": imdb_score,
        "actors": actors
    }
    movies.append(new_movie)

def delete_movie(movies, movie_id):
    del movies[movie_id]

def update_movie_imdb(movies, movie_id, imdb_score):
    movies[movie_id]["imdb_score"] = imdb_score