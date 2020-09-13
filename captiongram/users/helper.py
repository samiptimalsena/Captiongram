import os
import secrets
from PIL import Image
from flask import url_for, current_app


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/temp', picture_fn)

    i = Image.open(form_picture)
    i.save(picture_path)

    return picture_fn


#helper function to check the file extention 
def allowed_file(filename):
    UPLOAD_FOLDER = '/media'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
