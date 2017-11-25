import webbrowser

class Movie():

# Class Method for Movie Info

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.story_line = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Method for opening the Trailer URL
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

# Method for opening the Movie Poster Image
    def show_poster(self):
        webbrowser.open(self.poster_image_url)