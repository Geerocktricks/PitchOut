from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Express your thoughts.',validators = [Required()])
    submit = SubmitField('Submit')

class AddPitchForm(FlaskForm):
    title = StringField("Title", validators = [Required()])
    pitch = TextAreaField("PitchOut", validators = [Required()])
    category = StringField('Categories')
    submit = SubmitField("Add pitch")

class AddComment(FlaskForm):
    content = TextAreaField("Add comment")
    submit = SubmitField("Add")