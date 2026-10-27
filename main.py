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
                repo.save_users(users, USERS_PATH)
                repo.save_movies(movies, MOVIES_PATH)
                repo.save_watch(watchlists, WATCH_PATH)
                break
            else:
                print("Invalid input. Please try again.\n")

        elif current_menu == "user":
            # Add a user with name and age
            if option == "1":
                name, age = ui.get_user_credentials()
                if name is not None:
                    logic.add_user(users, name, age)
                    clear()
                    print("User added successfully.\n")

            # Delete a user by selecting them from the list of users
            elif option == "2":
                print("Enter the ID of the user you want to delete.\n")
                user_id = ui.select_user(users)
                if user_id is not None:
                    logic.delete_user(users, user_id)
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
                        clear()
                        print("User updated successfully.\n")

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
                    clear()
                    print("Movie added successfully.\n")

            # Delete a movie by selecting it from the movie list
            elif option == "2":
                print("Enter the ID of the movie you want to delete.\n")
                movie_id = ui.select_movie(movies)
                if movie_id is not None:
                    logic.delete_movie(movies, movie_id)
                    clear()
                    print("Movie deleted successfully.\n")
            elif option == "3":
                print("Enter the ID of the Movie you want to edit.\n")
                movie_id = ui.select_movie(movies)
                if movie_id is not None:
                    imdb_score = ui.get_imdb_score()
                    if imdb_score is not None:
                        logic.update_movie_imdb(movies, movie_id, imdb_score)
                        clear()
                        print("Movie updated successfully.\n")
            elif option == "4":
                ui.display_movies(movies)
                print("")
            elif option == "0":
                current_menu = "main"
            else:
                print("Invalid input. Please try again.\n")
        """
        elif current_menu == "watch":
            if option == "1":

            elif option == "2":

            elif option == "3":

            elif option == "4":

            elif option == "5":

            elif option == "0":

            else:
                print("Invalid input. Please try again.")
        """
if __name__ == "__main__":
    main()