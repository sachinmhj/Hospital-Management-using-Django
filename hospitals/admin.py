from django.contrib import admin
from .models import HospitalRecord

# Register your models here.
@admin.register(HospitalRecord)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name','address','email']
    