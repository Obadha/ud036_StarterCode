import webbrowser

class MovieTrailers():
	#Declare instance variables
	def __init__(self, movie_title, movie_poster, movie_trailer):
		self.title = movie_title
		self.poster_image_url = movie_poster
		self.trailer_youtube_url = movie_trailer


	#The method responsible for opening the browser and rendering the
	#movie trailer page.
	def show_trailer(self):
		webbrowser.open(self.trailer)

