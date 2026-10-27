import os
import logic

def clear():
    os.system("clear")

# =======
# 0 MENUS
# =======

def display_current_menu(current_menu):
    if current_menu == "main":
        display_main_menu()
    elif current_menu == "user":
        display_user_menu()
    elif current_menu == "movie":
        display_movie_menu()
    elif current_menu == "watch":
        display_watch_menu()

def display_main_menu():
    print("Press 1 to open the User Management Menu")
    print("Press 2 to open the Movie Management Menu")
    print("Press 3 to open the Watch List Menu")
    print("Press 0 to close the application")

def display_user_menu():
    print("Press 1 to Add a User")
    print("Press 2 to Delete a User")
    print("Press 3 to Update a User")
    print("Press 4 to Display all Users")
    print("Press 0 to Go Back to the Main Menu")

def display_movie_menu():
    print("Press 1 to Add a Movie")
    print("Press 2 to Delete a Movie")
    print("Press 3 to Update the Rating of a Movie")
    print("Press 4 to Display all Movies")
    print("Press 0 to Go Back to the Main Menu")

def display_watch_menu():
    print("Press 1 to Add an Entry to the Watch List")
    print("Press 2 to Show watched Movies for a User")
    print("Press 3 to Search a Movie by an actor")
    print("Press 4 to Search Movies by their Rating")
    print("Press 5 to Display all Watch Lists")
    print("Press 0 to Go Back to the Main Menu")

# ======
# COMUNE
# ======

def selection(array):
    try:
        selected = int(input().strip()) - 1
        if 0 <= selected < len(array):
            clear()
            return selected
    except ValueError:
        pass
    print("Invalid selection. Please try again.\n")
    return None

# =====
# USERS
# =====

def display_users(users):
    if len(users) == 0:
        print("No Users available.\n")
    else:
        for index, user in enumerate(users, start=1):
            print(f"ID: {int(index)}\tname: {user.get('name')}, age: {user.get('age')}")

def get_user_credentials():
    print("Enter the Name of the User:")
    name = input().strip()
    if name == "":
        print("Invalid Name. Please try again.\n")
        return None, None
    print("Enter the Age of the User:")
    try:
        age = int(input().strip())
        if 0 < age < 150:
            clear()
            return name, age
    except ValueError:
        pass
    print("Invalid Age. Please try again.\n")
    return None, None

def select_user(users):
    display_users(users)
    if len(users) != 0:
        return selection(users)
    return None

# ======
# MOVIES
# ======

def display_movies(movies):
    if len(movies) == 0:
        print("No Movies available.\n")
    else:
        for index, movie in enumerate(movies, start=1):
            print(f"ID: {index}\tname: {movie.get('name')}, release date: {movie.get('release_date')},"
                  f"IMDB Rating: {movie.get('imdb_score')}, Actors: {movie.get('actors')}")

def get_imdb_score():
    print("Enter the IMDB Rating")
    try:
        imdb_score = float(input().strip())
        if 0 <= imdb_score <= 10:
            return imdb_score
    except ValueError:
        pass
    print("Invalid IMDB Rating. Please try again.\n")
    return None

def get_movie_credentials():
    print("Enter the Name of the Movie:")
    name = input().strip()
    if name == "":
        print("Invalid Name. Please try again.\n")
        return None, None
    print("Enter the Release Date of the Movie as dd.mm.yyyy:")
    release_date = input().strip()
    if not logic.is_valid_date(release_date):
        print("Invalid Release Date. Please try again.\n")
        return None, None, None, None
    imdb_score = get_imdb_score()
    if imdb_score is None:
        return None, None, None, None
    print("Enter the name of the Actors, separated by ', ' :")
    actors_input = input().strip()
    actors = [actor.strip() for actor in actors_input.split(",") if actor.strip() != ""]
    return name, release_date, imdb_score, actors

def select_movie(movies):
    display_movies(movies)
    if len(movies) != 0:
        return selection(movies)
    return None


# =====
# WATCH
# =====


"""
watch_entry = {
    "user_name": "u",
    "movie_name": "m"
}

"""
