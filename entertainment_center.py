import fresh_tomatoes
import media
# Thor Ragnarok Movie Info
thor = media.Movie("Thor Ragnarok","It's about Thor",
                   "https://vignette.wikia.nocookie.net/marvel-cinematic-universe/images/5/58/Thor_Ragnarok_Poster.jpg/revision/latest?cb=20170513114458",
                   "https://www.youtube.com/watch?v=v7MGUNV8MxU")

#Justice League Movie Info
justice_league = media.Movie("Justice League","SuperMan Story",
                             "https://pbs.twimg.com/media/DMcGU2PXkAIystn.jpg" ,
                             "https://www.youtube.com/watch?v=JsjtqpLbtvU")

#Kingsman Movie Info
kingsman_2 = media.Movie("Kingsman 2", " It's about Kingsman",
                         "https://fanart.tv/fanart/movies/343668/movieposter/kingsman-2-596dd64f37fcf.jpg",
                         "https://www.youtube.com/watch?v=7uoga--HlnY")

# List of Movies
movies = [thor, justice_league, kingsman_2]

# Movie Info to be displayed on HTML format using fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
