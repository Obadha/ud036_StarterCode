import webbrowser

class MovieTrailers():
	def __init__(self, movie_title, movie_poster, movie_trailer):
		self.title = movie_title
		self.poster_image_url = movie_poster
		self.trailer_youtube_url = movie_trailer

#Have categories for different movies.
	def show_trailer(self):
		webbrowser.open(self.trailer)

