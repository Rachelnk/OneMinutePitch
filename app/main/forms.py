from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField,SelectField
from wtforms.validators import InputRequired
from ..models import Pitch,Comment

class PitchForm(FlaskForm):
    title = StringField ('Title', validators= [InputRequired()])
    post = TextAreaField('Pitch',validators=[InputRequired()])
    category = SelectField('Category',choices=[('Job','Job'),('Business','Business'),('Advertisement','Advertisement')])
    submit = SubmitField('Add Pitch')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment on the post',validators=[InputRequired()])
    submit = SubmitField('Add Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a bit about yourself',validators=[InputRequired()])
    submit = SubmitField('Add Bio')
