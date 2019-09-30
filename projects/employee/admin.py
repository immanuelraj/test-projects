from django.contrib import admin
from .models import Employees,Departments,DeptEmp,Titles,Salaries

admin.site.register(Employees)
admin.site.register(Departments)
admin.site.register(DeptEmp)
admin.site.register(Titles)
admin.site.register(Salaries)
