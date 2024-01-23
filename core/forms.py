from django import forms


class CreateLinkForm(forms.Form):
    original_url = forms.URLField(max_length=2000)
