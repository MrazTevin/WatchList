from flask import render_template
from app import app
from .request import get_movies
# views


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # get popular Movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    print(popular_movies)
    title = 'Home - Welcome to the best Movie Review Website Online'
    return render_template('index.html', title=title, popular=popular_movies, upcoming=upcoming_movie, now_showing=now_showing_movie)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''view movie function that returns view movie details
        page and it's data'''
    return render_template('movie.html', id=movie_id)
