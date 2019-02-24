from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=40)])
    image = FileField('Attach Picture', validators=[FileAllowed(['jpg', 'png'])])
    content = TextAreaField('Write whatever you want to share', validators=[DataRequired()])
    submit = SubmitField('Post')
