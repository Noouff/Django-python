from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext


# Create your views here.

def _(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text

def home(request):
    trans = _(language='ar')
    return render(request, 'employee_register/index.html', {'trans': trans})

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", 
                {
                    'form': form,
                    'submit': _('Submit'),
                    'Back to list': _('Back to list')
                }
            )

    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
