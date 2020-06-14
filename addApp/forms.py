from django import forms
from addApp.models import Add

# Create the form class.
class AddressForm(forms.ModelForm):
    pincode = forms.CharField( max_length=6 , widget=forms.TextInput(attrs={'placeholder': '6 digits[0-9] PIN code'}))
    class Meta:
         model = Add
         fields = '__all__'