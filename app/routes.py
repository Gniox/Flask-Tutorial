from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Chalt'}
    posts = [
        {
            'author': {'username': 'Razor'},
            'body': 'I like Seattle!'
        },
        {
            'author': {'username': 'Tristan'},
            'body': 'I like videogames!'
        }
    ]
    return render_template('index.html', title='Home',user=user, posts = posts)