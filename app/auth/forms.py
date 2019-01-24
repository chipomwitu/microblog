from app.models import User

from flask_babel import _, lazy_gettext as _1
from flask_wtf import FlaskForm

from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    username=StringField(_1('Username'), validators=[DataRequired()])
    email=StringField(_1('Email'), validators=[DataRequired(), Email()])
    password=PasswordField(_1('Password'), validators=[DataRequired()])
    confirm=PasswordField(_1('Confirm Password'), validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField(_1('Register'))

    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please pick a different username.'))

    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please pick a different email address.'))

class LoginForm(FlaskForm):
    username=StringField(_1('Username'), validators=[DataRequired()])
    password=PasswordField(_1('Password'), validators=[DataRequired()])
    remember_me=BooleanField(_1('Remember Me'))
    submit=SubmitField(_1('Log In'))

class ResetPasswordRequestForm(FlaskForm):
    email=StringField(_1('Email'), validators=[DataRequired(), Email()])
    submit=SubmitField(_1('Request Password Reset'))

class ResetPasswordForm(FlaskForm):
    password=StringField(_1('Password'), validators=[DataRequired()])
    password2=StringField(_1('Confirm password'), validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField(_1('Reset Password'))
