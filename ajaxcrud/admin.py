from django.contrib import admin
from .models import employee_information


# Register your models here.
# admin.site.register(employee_information)
@admin.register(employee_information)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['em_name','em_email','em_phn']