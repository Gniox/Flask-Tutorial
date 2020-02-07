from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign in', form = form)
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