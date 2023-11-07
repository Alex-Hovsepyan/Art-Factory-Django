from django import forms
from .models import Contact

class ContactModelForm(forms.ModelForm):

    class Meta:

        model = Contact
        fields = ['username', 'email', 'message']