import os

def read_users(path):
    if not os.path.exists(path):
        return []
    users = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                user_credentials = line.split("|")
                user = {
                    "name": user_credentials[0],
                    "age": int(user_credentials[1])
                }
                users.append(user)
    return users

def read_movies(path):
    if not os.path.exists(path):
        return []
    movies = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                movie_credentials = line.split("|")
                actors = movie_credentials[3].split(",") if movie_credentials[3] != "" else []
                movie = {
                    "name": movie_credentials[0],
                    "release_date": movie_credentials[1],
                    "imdb_score": float(movie_credentials[2]),
                    "actors": actors
                }
                movies.append(movie)
    return movies

def read_watch(path):
    if not os.path.exists(path):
        return []
    watchlists = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                watch_credentials = line.split("|")
                watch_entry = {
                    "user_name": watch_credentials[0],
                    "movie_name": watch_credentials[1]
                }
                watchlists.append(watch_entry)
    return watchlists

def save_users(path, users):
    with open(path, "w") as file:
        for user in users:
            file.write(f"{user['name']}|{user['age']}\n")

def save_movies(path, movies):
    with open(path, "w") as file:
        for movie in movies:
            actors_str = ",".join(movie["actors"])
            line = f"{movie['name']}|{movie['release_date']}|{movie['imdb_score']}|{actors_str}"
            file.write(line + "\n")

def save_watch(path, watchlists):
    with open(path, "w") as file:
        for entry in watchlists:
            file.write(f"{entry['user_name']}|{entry['movie_name']}\n")