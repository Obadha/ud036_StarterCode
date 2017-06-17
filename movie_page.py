import fresh_tomatoes
import media

star_wars = media.MovieTrailers("Star Wars", "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",  # NOQA
	"https://www.youtube.com/watch?v=sGbxmsDFVnE")

lordoftherings = media.MovieTrailers("Lord Of The Rings", "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",  # NOQA
	"https://www.youtube.com/watch?v=V75dMMIW2B4")

transformers = media.MovieTrailers("Transformers", "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",  # NOQA
	"https://www.youtube.com/watch?v=6Vtf0MszgP8")

avengers = media.MovieTrailers("Avengers", "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",  # NOQA
	"https://www.youtube.com/watch?v=eOrNdBpGMv8")

xmen = media.MovieTrailers("X Men", "https://upload.wikimedia.org/wikipedia/en/0/0c/X-Men_Days_of_Future_Past_poster.jpg",  # NOQA
	"https://www.youtube.com/watch?v=pK2zYHWDZKo")

justiceLeague = media.MovieTrailers("Justice League", "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",  # NOQA
	"https://www.youtube.com/watch?v=OiAmnKUaNmc")


movies = [star_wars, lordoftherings, transformers, avengers, xmen,
justiceLeague ]
fresh_tomatoes.open_movies_page (movies)