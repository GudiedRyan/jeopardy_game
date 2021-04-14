from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class JeopardyForm(FlaskForm):
    # Need 5 topics, and then point values from 100 - 400?
    submit = SubmitField('Create')