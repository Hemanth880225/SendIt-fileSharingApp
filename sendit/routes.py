from werkzeug.utils import secure_filename
from sendit.models import FileUpload, Folder, User
from sendit import app,db
from flask import render_template,flash,redirect,url_for,request,abort
from datetime import datetime
from sendit.forms import FolderForm, RenameFolderForm, RenameFileForm, RegisterForm, LoginForm, UploadForm, UpdateAccountForm
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import os

ALLOWED_EXTENSIONS = {'png', 'jpg','jpeg','gif','pdf','txt','zip'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        return redirect(url_for("folders"))
    return render_template("home.html")

from sendit.forms import FolderForm
from sendit.models import Folder
from sendit.models import ist_time

@app.route('/folders', methods=['GET', 'POST'])
@login_required
def folders():
    form = FolderForm()
    user_folders = Folder.query.filter_by(user_id=current_user.id).all()
    form.parent_id.choices = [(0, 'None (Root Folder)')] + [(f.id,f.name) for f in user_folders]

    if form.validate_on_submit():
        folder_name = form.name.data
        parent_choice = form.parent_id.data
        parent_id = parent_choice if parent_choice != 0 else None

        new_folder = Folder(
            name=folder_name,
            created_at=ist_time(),
            parent_id = parent_id,
            user_id=current_user.id
        )

        db.session.add(new_folder)
        db.session.commit()

        flash('Folder created successfully!', 'success')
        return redirect(url_for('folders'))

    folders = Folder.query.filter_by(user_id=current_user.id, parent_id=None).all()

    return render_template('folders.html', form=form, folders=folders)


@app.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()

    form.folder_id.choices = [(f.id,f.name) for f in Folder.query.filter_by(user_id=current_user.id).all()]

    if form.validate_on_submit():

        file = form.file.data
        description = form.description.data
        folder_id  = form.folder_id.data

        if not allowed_file(file.filename):
            flash('Unsupported File Format','danger')
            return redirect(url_for('upload'))

        filename = secure_filename(file.filename)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        upload_record = FileUpload(
            filename=filename,
            description=description,
            folder_id = folder_id,
            user_id = current_user.id
        )

        db.session.add(upload_record)
        db.session.commit()

        flash('File uploaded successfully!', 'success')

        return redirect(url_for('uploads_by_folder', folder_id=folder_id))

    return render_template('upload.html' , form=form)


@app.route('/folders/<int:folder_id>')
@login_required
def uploads_by_folder(folder_id):
    folder = Folder.query.filter_by(id=folder_id, user_id=current_user.id).first_or_404()

    subfolders = folder.subfolders
    files = folder.files

    breadcrumbs = []

    current = folder

    while current:
        breadcrumbs.insert(0, current)
        current = current.parent

    return render_template(
        'uploads.html',
        folder=folder,
        files=files,
        subfolders=subfolders,
        breadcrumbs=breadcrumbs
    )


@app.route('/delete/<int:id>',methods=['POST'])
@login_required
def delete_file(id):
    file = FileUpload.query.get_or_404(id)

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    if os.path.exists(file_path):
        os.remove(file_path)

    db.session.delete(file)
    db.session.commit()

    flash('File deleted successfully!', 'success')

    return redirect(url_for('uploads_by_folder', folder_id=file.folder_id))


@app.route('/folder/delete/<int:id>',methods=['POST'])
@login_required
def delete_folder(id):
    folder = Folder.query.get_or_404(id)

    db.session.delete(folder)
    db.session.commit()

    flash('Folder deleted successfully!', 'success')

    return redirect(url_for('folders'))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_file(id):
    file = FileUpload.query.get_or_404(id)

    form = UploadForm()

    form.folder_id.choices = [(f.id, f.name) for f in Folder.query.filter_by(user_id=current_user.id).all()]

    if form.validate_on_submit():

        file.description = form.description.data

        if form.file.data:

            new_file = form.file.data

            filename = secure_filename(new_file.filename)

            new_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            file.filename = filename

        file.folder_id = form.folder_id.data

        db.session.commit()

        flash('File updated successfully!', 'success')

        return redirect(url_for('uploads_by_folder', folder_id=file.folder_id))

    elif request.method == 'GET':

        form.description.data = file.description
        form.folder_id.data = file.folder_id

    return render_template('update.html', form=form, file=file)


@app.route('/folder/rename/<int:id>', methods=['GET', 'POST'])
@login_required
def rename_folder(id):
    folder = Folder.query.get_or_404(id)

    form = RenameFolderForm()

    if form.validate_on_submit():

        folder.name= form.name.data

        db.session.commit()

        flash('Folder renamed successfully!', 'success')

        return redirect(url_for('folders'))

    elif request.method == 'GET':

        form.name.data = folder.name

    return render_template('rename_folder.html', form=form,folder=folder)


@app.route('/rename/<int:id>', methods=['GET', 'POST'])
@login_required
def rename_file(id):
    file = FileUpload.query.get_or_404(id)

    form = RenameFileForm()

    if form.validate_on_submit():

        file.filename = form.filename.data

        db.session.commit()

        flash('File renamed successfully!', 'success')

        return redirect(url_for('uploads_by_folder', folder_id=file.folder_id))

    elif request.method == 'GET':

        form.filename.data = file.filename

    return render_template('rename_file.html', form=form, file=file)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('folders'))

    form = RegisterForm()

    if form.validate_on_submit():

        hashed_pw = generate_password_hash(form.password.data)

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_pw
        )

        db.session.add(user)
        db.session.commit()

        flash('Account created successfully! Please log in.', 'success')

        return redirect(url_for('login'))

    return render_template('register.html', form=form)


from sendit import bcrypt

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('folders'))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):

            login_user(user)

            flash('Login successful!', 'success')

            next_page = request.args.get('next')

            return redirect(next_page) if next_page else redirect(url_for('folders'))

        else:

            flash('Login unsuccessful!', 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()

    flash('Logout successful!', 'info')

    return redirect(url_for('login'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)

    _,f_ext = os.path.splitext(form_picture.filename)

    picture_fn = random_hex + f_ext

    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    form_picture.save(picture_path)

    return picture_fn


@app.route('/account' , methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()

    if form.validate_on_submit():

        if form.picture.data:

            picture_file = save_picture(form.picture.data)

            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data

        db.session.commit()

        flash('Your account has been updated!', 'success')

        return redirect(url_for('account'))

    elif request.method == 'GET':

        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

    return render_template('account.html', image_file=image_file, form=form)