from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.models import User



class RegistrationForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(), Length(2, 20)])
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("password",
                             validators=[DataRequired()])
    confirm_password = PasswordField("password",
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one')


class LoginForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("password",
                             validators=[DataRequired()])
    remember = BooleanField()
    submit = SubmitField('Login In')
