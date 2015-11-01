import webbrowser


class Movie():
	"""The class Movie models the structure for data about my favorite
	movies."""
	def __init__(self, title, storyline, poster_image,
				trailer_youtube, imdb_score):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.imdb_score = imdb_score

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
