from django.forms import ModelForm
from .models import Manager, Employee


class ManagerCreationForm(ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'