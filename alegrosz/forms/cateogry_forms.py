from wtforms import SelectField, SubmitField

from alegrosz.forms.item_forms import NewItemForm
from alegrosz.utils.belongs_to_other_field_option import BelongsToOtherFieldOption


class CategoryForm(NewItemForm):
    category = SelectField('Category', coerce=int)
    subcategory = SelectField('Subcategory', coerce=int,
                              validators=[BelongsToOtherFieldOption(table='subcategories', belongs_to='category',
                                                                    message='Select different category')])
    submit = SubmitField("Submit")
