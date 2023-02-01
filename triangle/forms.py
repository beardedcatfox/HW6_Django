from django import forms

from .models import Person


class TriangleForm(forms.Form):
    legA = forms.IntegerField(required=True, min_value=1)
    legB = forms.IntegerField(required=True, min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
