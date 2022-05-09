from flask import render_template, request,redirect,url_for
from . import main
from flask_login import login_required,current_user,login_user,logout_user
from .forms import PitchdForm, CommentsForm, UpdateProfile
from ..models import User, Comment, Pitch
from .. import db


@main.route('/')
def index():
  product_pitch = Pitch.get_pitch('Product')
  interview_pitch = Pitch.get_pitch('Interview')
  promotion_pitch = Pitch.get_pitch('Promotion')
  pickup_pitch = Pitch.get_pitch('Pick-up')
  title = 'Home - Welcome to One Minute Pitch. '
  return render_template('index.html', title = title, pitches=product_pitch,interview_pitch=interview_pitch,promotion_pitch=promotion_pitch,pickup_pitch=pickup_pitch)
