from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField, DateField, FileField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf.file import FileField, FileAllowed

class ProfileForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired(), Length(min=2, max=40)])
    bio = TextAreaField('Bio')
    gender = RadioField('Gender', choices = [('M','Male'),('F','Female')], validators=[DataRequired()])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    cover = FileField('Cover Pic', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')
