import fresh_tomatoes
import media

star_wars = media.MovieTrailers("Star Wars", "poster", "www.youtube.com")

lordoftherings = media.MovieTrailers("Lord Of The Rings", "poster", "www.gmail.com")

movies = [star_wars, lordoftherings ]

fresh_tomatoes.open_movies_page (movies)