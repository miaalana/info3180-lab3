from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email, DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"required": "required"})
    email = StringField('Email', validators=[InputRequired(),Email()])
    subject = StringField('Subject', validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired()])

