from app.models import User

from flask_babel import _, lazy_gettext as _1
from flask_wtf import FlaskForm

from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class EditProfileForm(FlaskForm):
    username=StringField(_1('Username'), validators=[DataRequired()])
    about_me=TextAreaField(_1('About me'), validators=[Length(min=0, max=140)])
    submit=SubmitField(_1('Submit'))
    # cancel=SubmitField(_1('Cancel'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username=original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user=User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))

class PostForm(FlaskForm):
    post=TextAreaField(_1('Say something...'), validators=[DataRequired(), Length(min=1, max=140)])
    submit=SubmitField(_1('Submit'))
