from django import forms

class searchForm(forms.Form):
    search_term = forms.CharField(label='Search Term',max_length=20)