from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class ScrapperForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Name', validators=[DataRequired()])
    url = StringField('Site URL', validators=[DataRequired()])
    selector = StringField('Tag selector', validators=[DataRequired()])
    submit = SubmitField()
