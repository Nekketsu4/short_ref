from django import forms

from app.models import URL


class CreateShortURLForm(forms.ModelForm):

    url = forms.URLField(max_length=200, label="")

    class Meta:
        model = URL
        fields = ['url',]
