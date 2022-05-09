from unicodedata import category
from flask import render_template, request,redirect,url_for, abort
from . import main
from flask_login import login_required,current_user,login_user,logout_user
from .forms import PitchForm, CommentsForm, UpdateProfile
from ..models import User, Comment, Pitch
from .. import db


@main.route('/')
def index():
  pitches = Pitch.query.all()
  business= Pitch.query.filter_by(category = 'Business').all()
  job = Pitch.query.filter_by(category = 'Job').all()
  advertisement = Pitch.query.filter_by(category = 'Advertisment').all()
  title = 'Home - Welcome to One Minute Pitch. '
  return render_template('index.html', title = title, pitches=pitches, job=job,business=business, advertisement=advertisement)

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.index'))
