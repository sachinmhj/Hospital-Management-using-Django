from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .forms import HospitalDetailsForm
from .models import HospitalRecord
from django.views.generic import DeleteView

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import HospitalSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

def home(request):
    if request.method == "POST":
        hospital_form = HospitalDetailsForm(request.POST)
        if hospital_form.is_valid():
            hospital_form.save()
            return HttpResponseRedirect('/success/')
    else:
        hospital_form = HospitalDetailsForm()
    return render(request,'hospitals/home.html',{'hospitalForm':hospital_form})

def update(request, iden):
    user = HospitalRecord.objects.get(id = iden)
    hospital_form = HospitalDetailsForm(instance = user)
    if request.method == 'POST':
        hospital_form = HospitalDetailsForm(request.POST, instance = user)
        if hospital_form.is_valid():
            hospital_form.save()
        return HttpResponseRedirect('/success/')
    else:
        hospital_form = HospitalDetailsForm(instance = user)
        return render(request,'hospitals/update.html',{'hospitalform':hospital_form})
    
def allrecords(request):
    allRecords = HospitalRecord.objects.all()
    return render(request,'hospitals/hospital_list.html',{'records':allRecords})

class DeleteConfirm(DeleteView):
    model = HospitalRecord
    template_name = 'hospitals/deleteconfirm.html'
    success_url = '/records/'

def success(request):
    return render(request,'hospitals/success.html')

# for API
class Api(ListCreateAPIView):
    queryset = HospitalRecord.objects.all()
    serializer_class = HospitalSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
class RetrieveUpdateDel(RetrieveUpdateDestroyAPIView):
    queryset = HospitalRecord.objects.all()
    serializer_class = HospitalSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]