from django import forms

class HospitalDetailsForm(forms.Form):
    name = forms.CharField(label_suffix=" ")
    address = forms.CharField(label_suffix=" ")
    phone_number = forms.CharField(label_suffix=" ")
    email = forms.EmailField(label_suffix=" ")
    website = forms.URLField(required=False, label_suffix=" ", widget=forms.URLInput(attrs={'placeholder':'Optional'}))
    capacity = forms.IntegerField(label_suffix=" ")