# tracker/forms.py
from django import forms

class FoodNameForm(forms.Form):
    food_name = forms.CharField(label='Food Name', max_length=100, required=True)
