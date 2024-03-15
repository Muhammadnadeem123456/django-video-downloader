from django import forms
from .models import Todo


class formdata(forms.ModelForm):
    url = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={
        "class": "form-control", "id": "url",
    }))

    class Meta:
        model = Todo
        fields = ['url']
