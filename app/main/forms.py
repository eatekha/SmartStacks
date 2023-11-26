from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired


class NewCollectionForm(FlaskForm):
    collection_course = StringField(
        'The name of the course you\'re studying for.',
        validators=[DataRequired()])
    collection_description = TextAreaField(
        'Relevant topics related to the course.',
        validators=[DataRequired()])
    submit = SubmitField('Create Collection')
