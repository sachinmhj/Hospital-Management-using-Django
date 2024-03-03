from django import forms
from .models import HospitalRecord

class HospitalDetailsForm(forms.ModelForm):
    website = forms.URLField(required=False, widget=forms.URLInput(attrs={'placeholder':'Optional'}))
    def __init__(self, *args, **kwargs):
        super(HospitalDetailsForm, self).__init__(*args, **kwargs)
        self.label_suffix = '' 
    class Meta:
        model = HospitalRecord
        fields = '__all__'