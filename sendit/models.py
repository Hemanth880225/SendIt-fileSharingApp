from datetime import datetime
from sqlalchemy.testing.pickleable import User
from sendit import db, login_manager
from flask_login import current_user,UserMixin

import pytz


def ist_time():
    return datetime.now(pytz.timezone('Asia/Kolkata'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime,nullable=False ,default= ist_time())
    image_file = db.Column(db.String(120), nullable=False, default='default.webp')


    folders = db.relationship('Folder', backref='owner',lazy=True)
    files = db.relationship('FileUpload', backref='owner', lazy=True)

    def __repr__(self):
        return f"User ('{self.username}','{self.email}','{self.created_at}')"

class FileUpload(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    uploaded_at = db.Column(db.DateTime , default= ist_time(), nullable=False)
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"FileUpload ('{self.filename}','{self.uploaded_at}')"



class Folder(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default= ist_time)
    parent_id = db.Column(db.Integer, db.ForeignKey('folder.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subfolders = db.relationship('Folder', backref= db.backref('parent', remote_side=[id]), lazy=True)
    files = db.relationship('FileUpload', backref='folder', lazy = True)

    def __repr__(self):
        return f"Folder('{self.name}','{self.created_at}'"
