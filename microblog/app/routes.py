from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Agustin'}
    posts = [
        {
            'author': {'username': 'Jose'}, 
            'body': 'Having a great time in Disneyland!'
        },
        {
            'author' : {'username': 'Joaquin'},
            'body' : 'Anybody selling a couch?'
        }]
    return render_template('index.html', title='Home', user=user, posts=posts)