from flask import render_template
from . import main 
from flask_login import login_required


@main.route('/')
def index():
    '''View root page function that returns the index page and its data'''
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')

@main.route('/pitches')
def pitch():
    return render_template('pitch.html')

# added a dynamic route
# @app.route('/movie/<int:movie_id')
# def movie(movie_id):
#     '''____'''
#     return render_template('movie.html',id=movie_id)