from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField
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
    submit = SubmitField('Continue')

class CategoryForm(FlaskForm):
    question_100 = TextAreaField('100 Point Question', validators=[DataRequired()])
    answer_100 = StringField('Answer', validators=[DataRequired(), Length(min=1, max=50)])
    question_200 = TextAreaField('200 Point Question', validators=[DataRequired()])
    answer_200 = StringField('Answer', validators=[DataRequired(), Length(min=1, max=50)])
    question_300 = TextAreaField('300 Point Question', validators=[DataRequired()])
    answer_300 = StringField('Answer', validators=[DataRequired(), Length(min=1, max=50)])
    question_400 = TextAreaField('400 Point Question', validators=[DataRequired()])
    answer_400 = StringField('Answer', validators=[DataRequired(), Length(min=1, max=50)])
    question_500 = TextAreaField('500 Point Question', validators=[DataRequired()])
    answer_500 = StringField('Answer', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('Continue')

class ConfirmationForm(FlaskForm):
    private_game = BooleanField('Make Private?')
    submit = SubmitField('Finish')