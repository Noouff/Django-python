from django.contrib import admin
from .models import *


 

# Register your models here.





class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fullname','emp_code','mobile','position' )
admin.site.register(Employee,EmployeeAdmin)