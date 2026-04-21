from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_bcrypt import Bcrypt
from flask_login import  UserMixin, LoginManager

app = Flask(__name__)


app.config['SECRET_KEY'] = 'supersecretkey'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Hvarmac2005%40@localhost:5432/sendit_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads') #absolute path where files are saved
app.config['MAX_CONTENT_LENGTH'] =  256 * 1024 * 1024 #optional protection to block files over 256 MB



db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from sendit.models import FileUpload

@app.shell_context_processor
def make_shell_context_processor():
    return {'db': db , 'Fileupload': FileUpload}



from sendit.models import FileUpload
from sendit import routes

# ✅ ADD THIS EXACT BLOCK AT THE END
with app.app_context():
    db.create_all()


