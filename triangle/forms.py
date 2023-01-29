from django import forms


class TriangleForm(forms.Form):
    legA = forms.IntegerField(required=True, min_value=1)
    legB = forms.IntegerField(required=True, min_value=1)
