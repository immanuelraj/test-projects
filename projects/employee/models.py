from django.db import models
from django.contrib.admin.models import LogEntry

class Employees(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    emp_no = models.IntegerField(help_text='employee unique no.', unique=True, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=14, blank=True, null=True)
    last_name = models.CharField(max_length=16, blank=True, null=True)
    gender = models.CharField(choices=GENDER, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)

class Departments(models.Model):
    # DEPARTMENT = (
    #     ('d009', 'Customer Service'),
    #     ('d005', 'Development'),
    #     ('d002', 'Finance'),
    #     ('d003', 'Human Resources'),
    #     ('d001', 'Marketing'),
    #     ('d004', 'Production'),
    #     ('d006', 'Quality Management'),
    #     ('d008', 'Research'),
    #     ('d007', 'Sales'),
    # )
    dept_no = models.CharField(help_text='department no.', max_length=4, unique=True, blank=True, null=True)
    dept_name = models.CharField(max_length=40, unique=True, blank=True, null=True)

class DeptEmp(models.Model):
    emp_no = models.Foreigenkey(Employees, related_name = 'employee number', blank = True, null = True)
    dept_no = models.Foreigenkey(Departments, related_name= 'departemnt number', blank = True, null = True)

class Titles(models.Model):
    emp_no = models.Foreigenkey(Employees, related_name = 'employee number', blank = True, null = True)
    title = models.CharField(max_length=40, unique=True, blank=True, null=True)
    from_date = models.DateField(blank=True, unique=True, null=True)
    to_date = models.DateField()

class Salaries(models.Model):
    emp_no = models.Foreigenkey(Employees, related_name = 'employee number', on_delete=models.CASCADE, blank = True, null = True)
    salary = models.IntegerField(blank=True, null=True)
    from_date = models.DateField(blank=True, unique=True, null=True)
    to_date = models.DateField(blank=True, null=True)

