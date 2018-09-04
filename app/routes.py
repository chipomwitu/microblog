from app import app, db
from app.forms import EditProfileForm, LoginForm, RegisterForm
from app.models import User
from datetime import datetime
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen=datetime.utcnow()
        db.session.commit()

@app.route('/')
@app.route('/index')
@login_required
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

    return render_template('index.html', title='Home', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=RegisterForm()
    if form.validate_on_submit():
        user=User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Yaaaaaay! You are now registered!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page=url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Log In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<username>')
@login_required
def user(username):
    user=User.query.filter_by(username=username).first_or_404()
    posts=[
        {'author': user, 'body': 'No man steps into the same river twice.'},
        {'author': user, 'body': 'Appreciate the seasons and let them pass.'}
    ]

    return render_template('user.html', user=user, posts=posts)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form=EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.about_me=form.about_me.data
        db.session.commit()
        flash('Your changes have been saved!')
        return redirect(url_for('edit_profile'))

    elif request.method=='GET':
        form.username.data=current_user.username
        form.about_me.data=current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)
