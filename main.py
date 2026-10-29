import ui
import repo
import logic
import os

os.environ["TERM"] = "xterm-256color"

DATA_PATH = "data/"
USERS_PATH = DATA_PATH + "users.txt"
MOVIES_PATH = DATA_PATH + "movies.txt"
WATCH_PATH = DATA_PATH + "watchlists.txt"

def clear():
    os.system("clear")

def main():
    users = repo.read_users(USERS_PATH)
    movies = repo.read_movies(MOVIES_PATH)
    watchlists = repo.read_watch(WATCH_PATH)

    clear()
    current_menu = "main"

    while True:
        ui.display_current_menu(current_menu)
        option = input().strip()
        clear()
        if current_menu == "main":
            if option == "1":
                current_menu = "user"
            elif option == "2":
                current_menu = "movie"
            elif option == "3":
                current_menu = "watch"
            elif option == "0":
                repo.save_users(USERS_PATH, users)
                repo.save_movies(MOVIES_PATH, movies)
                repo.save_watch(WATCH_PATH, watchlists)
                break
            else:
                print("Invalid input. Please try again.\n")

        elif current_menu == "user":
            # Add a user with name and age
            if option == "1":
                name, age = ui.get_user_credentials()
                if name is not None:
                    logic.add_user(users, name, age)
                    repo.save_users(USERS_PATH, users)
                    clear()
                    print("User added successfully.\n")

            # Delete a user by selecting them from the list of users
            elif option == "2":
                print("Enter the ID of the user you want to delete.\n")
                user_id = ui.select_user(users)
                if user_id is not None:
                    logic.delete_user(users, user_id)
                    repo.save_users(USERS_PATH, users)
                    clear()
                    print("User deleted successfully.\n")

            # Update a user’s information (name or age)
            elif option == "3":
                print("Enter the ID of the User you want to edit.\n")
                user_id = ui.select_user(users)
                if user_id is not None:
                    name, age = ui.get_user_credentials()
                    if name is not None:
                        logic.update_user(users, user_id, name, age)
                        repo.save_users(USERS_PATH, users)
                        clear()
                        print("User updated successfully.\n")

            # Display all users
            elif option == "4":
                ui.display_users(users)
                print("")
            elif option == "0":
                current_menu = "main"
            else:
                print("Invalid input. Please try again.\n")

        elif current_menu == "movie":
            # Add a movie with name, release_date, imdb_rating, and a list of actors
            if option == "1":
                name, release_date, imdb_score, actors = ui.get_movie_credentials()
                if name is not None:
                    logic.add_movie(movies, name, release_date, imdb_score, actors)
                    repo.save_movies(MOVIES_PATH, movies)
                    clear()
                    print("Movie added successfully.\n")

            # Delete a movie by selecting it from the movie list
            elif option == "2":
                print("Enter the ID of the movie you want to delete.\n")
                movie_id = ui.select_movie(movies)
                if movie_id is not None:
                    logic.delete_movie(movies, movie_id)
                    repo.save_movies(MOVIES_PATH, movies)
                    clear()
                    print("Movie deleted successfully.\n")

            # Update the IMDb score of an existing movie
            elif option == "3":
                print("Enter the ID of the Movie you want to edit.\n")
                movie_id = ui.select_movie(movies)
                if movie_id is not None:
                    imdb_score = ui.get_imdb_score()
                    if imdb_score is not None:
                        logic.update_movie_imdb(movies, movie_id, imdb_score)
                        repo.save_movies(MOVIES_PATH, movies)
                        clear()
                        print("Movie updated successfully.\n")

            # Display all movies
            elif option == "4":
                ui.display_movies(movies)
                print("")
            elif option == "0":
                current_menu = "main"
            else:
                print("Invalid input. Please try again.\n")

        elif current_menu == "watch":
            # Add an entry to the watch list
            if option == "1":
                user_name, movie_name = ui.get_watch_credentials(users, movies)
                if user_name is not None:
                    logic.add_watch_entry(watchlists, user_name, movie_name)
                    repo.save_watch(WATCH_PATH, watchlists)
                    clear()
                    print("Entry added successfully.\n")

            # Display all movies watched by a specific user
            elif option == "2":
                user_name = ui.get_user_name()
                if logic.check_if_user_exists(users, user_name):
                    ui.display_movies_watched_by_user(watchlists, user_name)
                else:
                    print(f"User {user_name} does not exist. Please try again.\n")

            # List all movies featuring a specific actor
            elif option == "3":
                actor = ui.get_actor_name()
                ui.display_movies_with_actor(movies, actor)

            # Show all movies with an IMDb rating above a given threshold
            elif option == "4":
                imdb_score = ui.get_imdb_score()
                if imdb_score is not None:
                    ui.display_movies_with_rating(movies, imdb_score)
            elif option == "5":
                ui.display_watchlists(watchlists)
            elif option == "0":
                current_menu = "main"
            else:
                print("Invalid input. Please try again.\n")

if __name__ == "__main__":
    main()