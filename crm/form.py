from django import forms

class OrderForm (forms.Form):
    name=forms.CharField(max_length=200, label='Ваше имя', widget=forms.TextInput(attrs={'class':'form-control'}))
    phone=forms.CharField(max_length=30, label='Ваше номер', widget=forms.TextInput(attrs={'class':'form-control'}))

