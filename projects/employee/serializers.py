from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

class EmployeeSerializer(serializers.Serializer):

    class Meta:
        model = Employee
        fields = ('__all__')


class DepartmentsSerializer(serializers.Serializer):

    class Meta:
        model = Departments
        fields = ('__all__')

class DeptEmprializer(serializers.Serializer):

    class Meta:
        model = DeptEmp
        fields = ('__all__')

class TitlesSerializer(serializers.Serializer):

    class Meta:
        model = Titles
        fields = ('__all__')

class SalariesSerializer(serializers.Serializer):

    class Meta:
        model = Salaries
        fields = ('__all__')


