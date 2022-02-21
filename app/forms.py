import email
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Email



class ContactForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email",validators=[Email(),DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    msg = StringField("Message", validators=[DataRequired()])

