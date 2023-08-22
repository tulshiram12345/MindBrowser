from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Manager, Employee
from .forms import ManagerCreationForm, EmployeeForm


# Create your views here.

def home(request):
    employees = Employee.objects.all()
    context = {"employees": employees}
    return render(request, 'manager/employee_details.html', context)

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            manager = Manager.objects.get(email=email)
            if manager and manager.password == password:
                return redirect('home')
            else:
                messages.error(request, 'Email OR password does not exit')
        except:
            messages.error(request, 'Manager does not exist')

    context = {'page': page}
    return render(request, 'manager/login_register.html', context)


def registerPage(request):
    form = ManagerCreationForm()

    if request.method == 'POST':
        form = ManagerCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'manager/login_register.html', {'form': form})


def addEmployee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'manager/add_employee.html', context)



def updateEmployee(request, pk):
    emp = Employee.objects.get(empid=pk)
    form = EmployeeForm(instance=emp)

    if request.method == 'POST':
        emp.empid = request.POST.get('empid')
        emp.mobile = request.POST.get('mobile')
        emp.firstname = request.POST.get('firstname')
        emp.lastname = request.POST.get('lastname')
        emp.address = request.POST.get('address')
        emp.dob = request.POST.get('dob')
        emp.city = request.POST.get('city')
        emp.company = request.POST.get('company')
        emp.save()
        return redirect('home')

    context = {'form': form, 'employee': emp}
    return render(request, 'manager/update_employee.html', context)



def deleteEmployee(request, pk):
    room = Employee.objects.get(empid=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'manager/delete.html', {'obj': room})

