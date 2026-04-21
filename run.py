# from sendit import app

# if __name__ == "__main__":
#     app.run(debug=True)

from sendit import app, db
import os

# Ensure upload folder exists (VERY IMPORTANT for Render)
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Create database tables
with app.app_context():
    db.create_all()

# Enable proper error logging
app.config['PROPAGATE_EXCEPTIONS'] = True

if __name__ == "__main__":
    app.run(debug=True)