from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class JeopardyForm(FlaskForm):
    category_1 = StringField('Category 1', validators=[DataRequired(), Length(min=2, max=50)])
    category_2 = StringField('Category 2', validators=[DataRequired(), Length(min=2, max=50)])
    category_3 = StringField('Category 3', validators=[DataRequired(), Length(min=2, max=50)])
    category_4 = StringField('Category 4', validators=[DataRequired(), Length(min=2, max=50)])
    category_5 = StringField('Category 5', validators=[DataRequired(), Length(min=2, max=50)])
    category_6 = StringField('Category 6', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=50)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create')