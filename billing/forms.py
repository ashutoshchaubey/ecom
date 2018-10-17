from .models import Billings, Content
from django import forms

class BillingForm(forms.ModelForm):
    full_name = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length=254)
    billing_addr = forms.CharField(max_length=500)
    shipping_addr = forms.CharField(max_length=500)
    pincode = forms.IntegerField()
    phone_number = forms.IntegerField()
    
    class Meta:
        model = Billings
        fields = ('full_name', 'email', 'billing_addr','shipping_addr', 'pincode', 'phone_number')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('image', 'name_of_item')
