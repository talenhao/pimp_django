from django import forms


class SearchForm(forms.Form):
    cmdline = forms.CharField(required=False)

