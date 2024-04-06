from django.shortcuts import render, redirect
from myapp.forms import EmployeeForm
from myapp.models import Employee


# Create your views here.

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})


def edit(request, eid):
    employee = Employee.objects.get(id=eid)
    return render(request, 'edit.html', {'employee': employee})


def update(request, eid):
    employee = Employee.objects.get(id=eid)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})


def destroy(request, eid):
    employee = Employee.objects.get(id=eid)
    employee.delete()
    return redirect("/show")
