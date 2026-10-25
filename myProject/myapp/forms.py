from django import forms

class InputForm(forms.Form):
    name = forms.CharField(label="Name", min_length=3, )
    email = forms.EmailField(label="Email")
    city = forms.CharField(label="City")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
