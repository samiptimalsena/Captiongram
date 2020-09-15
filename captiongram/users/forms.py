from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user


from  captiongram.models import User

class RegistrationForm(FlaskForm):
    first_name = StringField('Firstname',validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Lastname',validators=[DataRequired(), Length(min=2, max=20)])                           
    email = StringField('Email',validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


    
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired(),Length(min=2, max=120)])

    submit = SubmitField('Post')
    