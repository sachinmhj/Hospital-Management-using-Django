from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import HospitalDetailsForm
from .models import HospitalRecord

# Create your views here.
def home(request):
    allRecords = HospitalRecord.objects.all()
    if request.method == "POST":
        hospital_form = HospitalDetailsForm(request.POST)
        if hospital_form.is_valid():
            cleanedData = hospital_form.cleaned_data
            name = cleanedData['name']
            address = cleanedData['address']
            phone = cleanedData['phone_number']
            email = cleanedData['email']
            website = cleanedData['website']
            capacity = cleanedData['capacity']
            saveData = HospitalRecord(name=name,address=address,phone_number=phone,email=email,website=website,capacity=capacity)
            saveData.save()
            return HttpResponseRedirect('/success/')
    else:
        hospital_form = HospitalDetailsForm()
    return render(request,'hospitals/home.html',{'hospitalForm':hospital_form,'records':allRecords})

def success(request):
    return render(request,'hospitals/success.html')
