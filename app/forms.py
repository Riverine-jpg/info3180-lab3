import email
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired, Email



class ContactForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()],name = "Full Name")
    email = StringField("Email",validators=[Email(),DataRequired()],name="Email")
    subject = StringField("Subject", validators=[DataRequired()],name="Subject")
    msg = TextAreaField("Message", validators=[DataRequired()],name="Message")


