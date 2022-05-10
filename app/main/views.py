from flask import render_template
from . import main 


@main.route('/')
def index():
    '''View root page function that returns the index page and its data'''
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')

# added a dynamic route
# @app.route('/movie/<int:movie_id')
# def movie(movie_id):
#     '''____'''
#     return render_template('movie.html',id=movie_id)