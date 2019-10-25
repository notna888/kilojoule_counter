from django import forms


class IngredientForm(forms.Form):
    ingredient_name = forms.CharField()
    ingredient_kj = forms.FloatField()
