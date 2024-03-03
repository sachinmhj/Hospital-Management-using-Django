from django import forms
from .models import HospitalRecord

class HospitalDetailsForm(forms.ModelForm):
    website = forms.URLField(required=False, widget=forms.URLInput(attrs={'placeholder':'Optional'}))
    class Meta:
        model = HospitalRecord
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ' '
    def clean(self):
        cleaned_data = super().clean()
        capacity = cleaned_data.get('capacity')
        if capacity and capacity < 0:
            return self.add_error('capacity','Please enter positive number.')
