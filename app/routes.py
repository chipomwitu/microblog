from app import app
from flask import flash, redirect, render_template, url_for
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Log In', form=form)
