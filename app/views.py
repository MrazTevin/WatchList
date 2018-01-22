from flask import render_template
from app import app
# views


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message = 'Hello World'
    return render_template('index.html', message=message)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''view movie function that returns view movie details
        page and it's data'''
    return render_template('movie.html', id=movie_id)
