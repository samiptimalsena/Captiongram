import os
from PIL import Image

from flask import current_app as app
from flask import render_template, url_for, flash, redirect, request, Blueprint, session
from flask_login import login_user, current_user, logout_user, login_required

#image uploads imports 
from werkzeug.utils import secure_filename
from datetime import datetime

#custom modues 
from captiongram import db, bcrypt,login_manager
from captiongram.users.forms import RegistrationForm, LoginForm
from captiongram.models import User,Post
from . import helper

#caption generation part
from captiongram.utils import caption_provider   


users = Blueprint('users', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@users.route('/',methods=['GET', 'POST'])
@users.route('/login',methods=['GET', 'POST'])
def index():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for('users.home'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # login_user(user, remember=form.remember.data)
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('users.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    
    return render_template('index.html',form=form)

 
@users.route('/register',methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        
        # redirect to verification check
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Bummer, email {} already taken.'.format(form.email.data), 'danger')
            return render_template('register.html',form=form)
        
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data, 
            password=hashed_password,
        )

        db.session.add(user)
        db.session.commit()

        
        flash('Your account has been created! Please log in to countinue', 'success')
        return redirect(url_for('users.index'))

    
    return render_template('register.html',form=form)


@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.index'))


@users.route("/home")   
@login_required
def home():
    #get captions
    posts = Post.query.order_by(Post.up_loaded.desc()).all()
    like_counts=[len(post.LikedBy) for post in posts ]
    print(posts)
    print(like_counts)

    #get user info 
    user_info = {
        "name":current_user.first_name +" "+ current_user.last_name,
        "email":current_user.email
    }
    posts=zip(posts,like_counts)

    return render_template('home.html',user=user_info,posts=posts)



@users.route("/add_captions",methods=['GET', 'POST'])
@login_required
def add_captions():
    
    if request.method == 'POST':
        temp_path = os.path.join(app.root_path,'static/temp')
        for fname in os.listdir(temp_path):
            os.remove(os.path.join(temp_path,fname))  #deleting any image that exist in the temp directory

        if 'file' not in request.files:
            flash('No suppored image uploaded','danger')
            return redirect(request.url)
        file = request.files['file']
        
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No suppored image uploaded',danger)
            return redirect(request.url)

        if file and helper.allowed_file(file.filename):
            picture_file = helper.save_picture(file)

            #picture uploaded  
            return redirect(url_for('users.confirm_captions',rawcaption=picture_file))

    #get user info 
    user_info = {
        "name":current_user.first_name +" "+ current_user.last_name,
        "email":current_user.email
    }

    return render_template('add_caption.html',user=user_info)


@users.route("/confirm_captions/<string:rawcaption>")
@login_required
def confirm_captions(rawcaption):

    cpation_text = caption_provider.generate_caption(rawcaption)


    #get user info 
    user_info = {
        "name":current_user.first_name +" "+ current_user.last_name,
        "email":current_user.email,
        "image_path":rawcaption,
        "caption":cpation_text
    }

    return render_template('confirm_gen.html',user=user_info)

@users.route("/commit_captions/<string:rawcaption>/<string:caption_text>")
@login_required
def commit_captions(rawcaption,caption_text):

    image = rawcaption
    text = caption_text
    user_name = current_user.first_name +" "+current_user.last_name
    user_id = current_user.id

    temp_image_path = os.path.join(app.root_path, 'static/temp', image)
    caption_image_path=os.path.join(app.root_path,'static/captions',image)
    i = Image.open(temp_image_path)
    i.save(caption_image_path)


    #create instance & write to the model 
    post = Post(
        caption = text,
        caption_image = image,
        user_id = user_id,
        user_name = user_name,
        up_loaded = datetime.now()
    )

    db.session.add(post)
    db.session.commit()

    flash('Your pic sucessfully uploaded :D', 'success')    

    return redirect(url_for('users.home'))

@users.route('/like/<int:post_id>/<action>')
@login_required
def like_action(post_id, action):
    post = Post.query.filter_by(id=post_id).first_or_404()
    if action == 'like':
        current_user.like_post(post)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(post)
        db.session.commit()
    return redirect(url_for('users.home'))