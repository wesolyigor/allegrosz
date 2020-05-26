from wtforms import SelectField, SubmitField

from alegrosz.forms.item_forms import NewItemForm


class CategoryForm(NewItemForm):
    category = SelectField('Category', coerce=int)
    subcategory = SelectField('Subcategory', coerce=int)
    submit = SubmitField("Submit")


