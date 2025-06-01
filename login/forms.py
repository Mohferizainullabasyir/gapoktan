from django import forms
from django.contrib.auth import authenticate

class NIKLoginForm(forms.Form):
    nik = forms.CharField(label='NIK', max_length=16)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        nik = self.cleaned_data.get('nik')
        password = self.cleaned_data.get('password')
        user = authenticate(nik=nik, password=password)
        if not user:
            raise forms.ValidationError("NIK atau password salah")
        self.user = user
        return self.cleaned_data
