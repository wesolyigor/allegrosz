from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, FileField, DecimalField


class NewItemForm(FlaskForm):
    title = StringField('Title')
    description = TextAreaField('Description')
    price = DecimalField('Price')
    image = FileField('Image')
    category = SelectField('Category', coerce=int)
    subcategory = SelectField('Subcategory', coerce=int)
    submit = SubmitField('Submit')
