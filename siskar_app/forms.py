from django import forms

CHOICES = [('1','Ya'),('0','Tidak')]

class FormName(forms.Form):
    attrib_1 = forms.CharField(label='1. Gejala1', widget=forms.RadioSelect(choices=CHOICES))