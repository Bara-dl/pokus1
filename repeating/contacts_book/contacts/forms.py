from django import forms
from .models import Contact


class ContactSearchForm(forms.Form):
    contact_name = forms.CharField(label='Contact name', max_length=100)



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
