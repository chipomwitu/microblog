from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index(): 
    posts=[
        {
            'author': {'username': 'Marundu'}, 
            'body': 'Discomfitting deja vu'
        },
        {
            'author': {'username': 'Rufus'},
            'body': 'Where has time gone?'
        }
    ]
    user={'username': 'chipomwitu'}
    
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html', title='Log In', form=form)
