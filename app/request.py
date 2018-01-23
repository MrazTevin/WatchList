from app import app
import urllib.request,json
from models import movie

Movie = movie.Movie
# getting api api_key
api_key = app.config['MOVIE_API_KEY']

# getting the movie based url
base_url = app.config["MOVIE_API_BASE_URL"]
