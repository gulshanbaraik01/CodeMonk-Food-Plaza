from django import forms
from .models import recipe_table

class recipe_form(forms.ModelForm):
    class Meta:
        model=recipe_table
        fields=('recipe_name' ,
        'recipe_type','ingredient','description'
        ,'process_of_making','picture')

      

