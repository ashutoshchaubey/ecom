# from . import models as md
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    from_email=forms.EmailField(required=True, max_length=254, widget=forms.TextInput())
    subject=forms.CharField(required=True, max_length=100, widget=forms.TextInput)
    message=forms.CharField(required=True, max_length=2000, widget=forms.Textarea())

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        subject = cleaned_data.get('subject')
        from_email = cleaned_data.get('from_email')
        message = cleaned_data.get('message')
        if not subject and not from_email and not message:
            raise forms.ValidationError('You have to write something ... ')

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# class SpecificationsForm(forms.ModelForm):
#   class Meta:
#       model = Specifications