from django import forms
from django.core import validators



class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Please verify the EMAIL")
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email =all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if vmail != email:
            raise forms.ValidationError("Make Sure Emails Match!")
