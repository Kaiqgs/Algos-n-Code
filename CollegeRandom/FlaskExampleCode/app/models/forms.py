from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, RadioField, FloatField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])
    rememberMe = BooleanField("rememberMe")

class SignupForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])

class AddVeterinaryForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    age = IntegerField("age", validators=[DataRequired()])
    gender = RadioField("gender", coerce=int)
    email = StringField("email", validators=[DataRequired()])

class AddPetForm(FlaskForm):
    name = StringField("name",validators=[DataRequired()])
    age = IntegerField("age", validators=[DataRequired()])
    race = StringField("race",validators=[DataRequired()])
    gender = RadioField("gender", coerce=int)
    owner_name = StringField("owner_name", validators=[DataRequired()])

class AddServiceForm(FlaskForm):
    veterinarian_name = SelectField("veterinarian_name", coerce=int)
    pet_name = SelectField("pet_name",coerce=int)
    price = FloatField("price",validators=[DataRequired()])
    description = TextAreaField("description", validators=[DataRequired()])
