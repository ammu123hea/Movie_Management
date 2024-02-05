#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Movie:
    def __init__(self, title, genre, year,language,rating=None):
        self.title = title
        self.genre = genre
        self.year = year
        self.language=language
        self.rating = rating
    def set_rating(self, rating):
        self.rating = rating


class MovieManager:
    def __init__(self):
        self.movies = []
        self.booking_details = {}# Store booking details
        self.wishlist = []  # Adding the wishlist attribute

    def add_movie(self, title, genre, year,language,rating=None):
        movie = Movie(title, genre, year,language,rating)
        self.movies.append(movie)
        print(f"{title} added to the movie list.")

    def view_movies(self):
        if not self.movies:
            print("No movies available.")
        else:
            print("Movie List:")
            for movie in self.movies:
                print(f"{movie.title} - {movie.genre} - {movie.year}-{movie.language}-{movie.rating}")
    def set_movie_rating(self, title, rating):
        movie = next((m for m in self.movies if m.title.lower() == title.lower()), None)
        if movie:
            movie.set_rating(rating)
            print(f"Rating set for {title}.")
        else:
            print(f"No movie found with the title: {title}.")
       

    def filter_by_genre(self, genre):
        filtered_movies = [movie for movie in self.movies if movie.genre.lower() == genre.lower()]
        if not filtered_movies:
            print(f"No movies found for the genre: {genre}.")
        else:
            print(f"Movies in the {genre} genre:")
            for movie in filtered_movies:
                print(f"{movie.title} - {movie.year}-{movie.language}")

    def filter_by_language(self, language):
        filtered_movies = [movie for movie in self.movies if movie.language.lower() == language.lower()]
        if not filtered_movies:
            print(f"No movies found for the language: {language}.")
        else:
            print(f"Movies in {language} language:")
            for movie in filtered_movies:
                print(f"{movie.title} - {movie.genre} - {movie.year}")
                
    def filter_by_rating(self,rating):
        filtered_movies=[movie for movie in self.movies if movie.rating==rating]
        if not filtered_movies:
            print(f"No movies found for the ratings:{rating}.")
        else:
            print(f"Movies in {rating} rating:")
            for movie in filtered_movies:
                print(f"{movie.title}-{movie.rating}")

    def add_to_wishlist(self, title):
        self.wishlist.append(title)
        print(f"{title} added to your wishlist.")

    def view_wishlist(self):
        if not self.wishlist:
            print("Your wishlist is empty.")
        else:
            print("Wishlist:")
            for title in self.wishlist:
                print(title)

    def cancel_booking(self, title,screen,timing,num_tickets):
        key = (title, timing, screen,num_tickets)
        if key in self.booking_details:
            del self.booking_details[key]
            print("Booking canceled successfully.")
        else:
            print("No booking found for the specified details.")


# Example
movie_manager = MovieManager()
movie_manager.add_movie("Inception", "Sci-Fi", 2010,"English")
movie_manager.add_movie("The Dark Knight", "Action", 2008,"English")
movie_manager.add_movie("Titanic", "Romance", 1997,"English")
movie_manager.add_movie("Upadyaksha", "Romance", 2024,"Kannada")
movie_manager.add_movie("Hanuman", "Action", 2024,"Telugu")
movie_manager.add_movie("Salaar", "Action", 2023,"Telugu")
movie_manager.add_movie("Bachelor Party", "Comedy", 2024,"Kannada")
movie_manager.add_movie("Ghost", "Action", 2023,"Kannada")
movie_manager.add_movie("Thathsama Tadhbava", "Suspense", 2023,"Kannada")
movie_manager.add_movie("Nanni", "Horror", 2023,"Telugu")
movie_manager.add_movie("Jessy", "Horror", 2023,"Telugu")
movie_manager.view_movies()
# Set ratings for movies
movie_manager.set_movie_rating("Inception", 4.5)
movie_manager.set_movie_rating("The Dark Knight", 5.0)
movie_manager.set_movie_rating("Titanic", 4.0)
movie_manager.set_movie_rating("Upadyaksha", 5.0)
movie_manager.set_movie_rating("Hanuman", 5.0)
movie_manager.set_movie_rating("Salaar", 4.3)
movie_manager.set_movie_rating("Bachelor Party", 5.0)
movie_manager.set_movie_rating("Ghost", 4.5)
movie_manager.set_movie_rating("Thathsama Tadhbava", 3.0)
movie_manager.set_movie_rating("Nanni", 5.0)
movie_manager.set_movie_rating("Jessy", 5.0)
# View movies with ratings
print("*****")
movie_manager.view_movies()
# Adding movies to wishlist
print("********")
movie_manager.add_to_wishlist(input("Enter the movie you want to watch: "))
movie_manager.add_to_wishlist(input("Enter the movie you want to wish to watch: "))
movie_manager.view_wishlist()
print("*****")
genre_to_filter = input("Enter the genre to filter movies: ")
movie_manager.filter_by_genre(genre_to_filter)
# Filter by language
print("*****")
language_to_filter = input("Enter the language to filter movies: ")
movie_manager.filter_by_language(language_to_filter)
# Filter by rating
print("*******")
rating_to_filter = input("Enter the rating to filter movies: ")
movie_manager.filter_by_rating(rating_to_filter)
# Filter by rating
print("*******")
rating_to_filter = input("Enter the rating to filter movies: ")
movie_manager.filter_by_rating(rating_to_filter)



# Booking a movie ticket
global f
f = 0


def t_movie():
    global f
    f = f + 1
    print("Which movie do you want to watch?")
    print("1, Updayksha")
    print("2, Fighter")
    print("3, Gunntu Karam")
    print("4, Hanuman")
    print("5, Ghost")
    print("6, Jessy")
    print("7, Nanni")
    print("8, Titanic")
    print("9,The Dark Knight")
    print("10,Inception")
    print("11,Bachelor Party")
    print("12,Thathasama Thadbhava")
    print("13,Salaar")
    movie = int(input("Choose your movie: "))
    if movie == 13:
        center()
        theater()
        return 0
    if f == 1:
        theater()


def theater():
    print("Which screen do you want to watch movie: ")
    print("1, Flat Screen")
    print("2, Horizontal Curve")
    print("3, Torex Screen")
    print("4, 3D")
    screen = int(input("Choose your screen: "))
    ticket = int(input("Number of tickets do you want?: "))
    timing(screen, ticket)


def timing(screen, num_tickets):
    ticket_prices = {
        "1": 10.00,  # Example ticket prices
        "2": 12.50,
        "3": 15.00,
        "4": 18.00
    }

    time1 = {
        "1": "10.00-1.00",
        "2": "1.10-4.10",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
    }
    time2 = {
        "1": "10.15-1.15",
        "2": "1.25-4.25",
        "3": "4.35-7.35",
        "4": "7.45-10.45"
    }
    time3 = {
        "1": "10.30-1.30",
        "2": "1.40-4.40",
        "3": "4.50-7.50",
        "4": "8.00-10.45"
    }

    if screen == 1:
        print("Choose your time:")
        print(time1)
        t = input("Select your time:")
        x = time1[t]
        price = ticket_prices[t]
        total_price = price * num_tickets
        print(f"Successful! Enjoy movie at {x}. Total Price: ${total_price}")
        key = (input("title of the movie:"),screen,timing,num_tickets)  # Example booking details
        movie_manager.booking_details[key] = True
    elif screen == 2:
        print("Choose your time:")
        print(time2)
        t = input("Select your time:")
        x = time2[t]
        price = ticket_prices[t]
        total_price = price * num_tickets
        print(f"Successful! Enjoy movie at {x}. Total Price: ${total_price}")
    elif screen == 3:
        print("Choose your time:")
        print(time3)
        t = input("Select your time:")
        x = time3[t]
        price = ticket_prices[t]
        total_price = price * num_tickets
        print(f"Successful! Enjoy movie at {x}. Total Price: ${total_price}")
    else:
        print("Tickets not available")
    return 0


def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        locality()
    else:
        print("Wrong choice")


def center():
    print("Which theater do you wish to see the movie? ")
    print("1, Inox")
    print("2, Icon")
    print("3, PVR")
    print("4, Back")
    screen = int(input("Choose your option: "))
    movie(screen)
    return 0


def locality():
    print("Hi welcome to movie ticket booking: ")
    print("***Booking a Movie Ticket***")
    print("Where do you want to watch the movie?:")
    print("1, Rajajinagar")
    print("2, Marathalli ")
    print("3, MG Road")
    print("4, Doddanekkundi")
    place = int(input("choose your option: "))
    if place == 1:
        center()
    elif place == 2:
        center()
    elif place == 3:
        center()
    elif place == 4:
        center()
    else:
        print("wrong choice")


locality()

# Add an option for cancellation
cancel_option = input("Do you want to cancel your booking? (yes/no): ")
if cancel_option.lower() == 'yes':
    title = input("Enter the movie title:")
    screen = input("Enter the screen:")
    timing_value = input("Enter the timing:")
    num_tickets = input("Enter the number of tickets:")
    movie_manager.cancel_booking(title,screen,timing_value,num_tickets)


# In[ ]:





# In[ ]:





# In[ ]:




