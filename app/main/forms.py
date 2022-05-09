from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField,SelectField
from wtforms.validators import InputRequired
from ..models import Pitch,Comment

class PitchdForm(FlaskForm):
    pitch = TextAreaField('Pitch',validators=[InputRequired()])
    category = SelectField('Category',choices=[('Interview','Interview'),('Pick-up','Pick-up'),('Product','Product'),('Promotion','Promotion')])
    submit = SubmitField('Add Pitch')

class CommentsForm(FlaskForm):
    comment = TextAreaField('comment on the post',validators=[InputRequired()])
    submit = SubmitField('Add Comment')

class UpdateProfile(FlaskForm):
    bio = StringField('About You',validators=[InputRequired()])
    submit = SubmitField('Add Bio')
