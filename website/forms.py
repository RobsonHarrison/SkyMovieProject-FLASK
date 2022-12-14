from wtforms import StringField, SubmitField, RadioField
from flask_wtf import FlaskForm

# inheritance
# BasicForm inherits from FlaskForm
# BasicForm is now a kind of FlaskForm

class BasicForm(FlaskForm):
    # instantiating various input fields
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField('Add Name')
    RadioField('Label', choices=[('value', 'description'), ('value_two', 'whatever')])