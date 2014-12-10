from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField()
    title = forms.CharField(max_length=50)
    text =  forms.CharField(widget=forms.Textarea)
    
    