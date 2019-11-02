from django import forms

class Register(forms.form):
    your_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    roll_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    branch = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    college = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    events = forms.ChoiceField(widget=forms.CheckboxInput(attrs={'class':'form-control'}))