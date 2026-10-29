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

def add_watch_entry(watchlists, user_name, movie_name):
    new_watch_entry = {
        "user_name": user_name,
        "movie_name": movie_name
    }
    watchlists.append(new_watch_entry)

def check_if_user_exists(users, user_name):
    for user in users:
        if user_name == user.get("name"):
            return True
    return False

def check_if_movie_exists(movies, movie_name):
    for movie in movies:
        if movie_name == movie.get("name"):
            return True
    return False

def get_movies_watched_by_user(watchlists, user_name):
    return [entry.get("movie_name") for entry in watchlists if entry.get("user_name") == user_name]

def get_movies_with_actor(movies, actor_name):
    matching_movies = []
    for movie in movies:
        actors_lower = [actor.lower() for actor in movie.get("actors", [])]
        if actor_name.lower() in actors_lower:
            matching_movies.append(movie)
    return matching_movies

def get_movies_with_rating(movies, min_score):
    return [movie for movie in movies if movie.get("imdb_score") >= min_score]

def get_sorted_watchlists(watchlists):
    return sorted(watchlists, key=lambda entry: entry.get("user_name"))