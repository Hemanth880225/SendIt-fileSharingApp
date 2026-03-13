from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, SubmitField , StringField , SelectField , PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sendit.models import User
from flask_login import current_user



from sendit.config import ALLOWED_EXTENSIONS
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data.strip()).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data.strip().lower()).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[ FileAllowed(['jpg', 'png','jpeg','webp'])])
    submit = SubmitField('Update')


    def validate_username(self, username):
        user = None
        new_name = username.data.strip()
        if current_user and new_name !=current_user.username:
            user = User.query.filter_by(username=new_name).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = None
        new_email = email.data.strip().lower()
        if current_user and new_email != current_user.email.lower():
            user = User.query.filter_by(email=new_email).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class FolderForm(FlaskForm):
    name = StringField('Folder Name', validators=[DataRequired(), Length(min=1, max=100)])
    parent_id = SelectField('Parent Folder', coerce=int)
    submit = SubmitField('Create Folder')



class UploadForm(FlaskForm):
    description = StringField('description', validators=[DataRequired(),Length(max=300)])
    file = FileField('Choose a file', validators=[FileRequired(message='Please select a file'),FileAllowed(ALLOWED_EXTENSIONS, message=f'Allowed:{",".join(ALLOWED_EXTENSIONS)}.')])
    folder_id = SelectField('Select Folder', coerce=int, validators=[DataRequired()])

    submit = SubmitField('Upload')

class RenameFileForm(FlaskForm):
    filename = StringField('New File Name', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Rename')

class RenameFolderForm(FlaskForm):
    name = StringField('New Folder Name', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Rename')