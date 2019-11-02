from django import forms

CHOICES = ['1','2','3']
class Register(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    roll_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    branch = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    college = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    events = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),choices=CHOICES)