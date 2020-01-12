from django import forms
from .models import order

class FoodForm(forms.ModelForm):

    class meta:
        model = order
        fields = '__all__'