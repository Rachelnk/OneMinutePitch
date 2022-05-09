from flask import render_template, request,redirect,url_for
from . import main
from flask_login import login_required,current_user,login_user,logout_user
from .forms import PitchdForm, CommentsForm, UpdateProfile
from ..models import User, Comment, Pitch


@main.route('/')
def index():
  title = 'Home - Welcome to One Minute Pitch. '
  return render_template('index.html', title = title)
