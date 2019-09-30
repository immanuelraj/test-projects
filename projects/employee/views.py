from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Employees, Departments, DeptEmp, Titles, Salaries
from .serializers import EmployeeSerializer, DepartmentsSerializer, DeptEmpSerializer, TitlesSerializer, SalariesSerializer

class EmployeesView(generics.ListAPIView):

    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentsView(generics.ListAPIView):
    
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

class DeptEmpView(generics.ListAPIView):
    
    queryset = DeptEmp.objects.all()
    serializer_class = DeptEmpSerializer

class TitlesView(generics.ListAPIView):
    
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer

class SalariesView(generics.ListAPIView):
    
    queryset = Salaries.objects.all()
    serializer_class = SalariesSerializer