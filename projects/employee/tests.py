from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Employees
from .serializers import EmployeeSerializer

# tests for views
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_employee(emp_no="", birth_date="", first_name="", last_name="", gender="", hire_date=""):
        if emp_no!="" and birth_date!="" and first_name!="" and last_name!="" and gender!="" and hire_date!="":
            Employees.objects.create(emp_no=emp_no, birth_date=birth_date, first_name=first_name, last_name=last_name, gender=gender, hire_date=hire_date)

    def setUp(self):
        # add test data
        self.create_song(1, datetime.now(), "brick", "rock", "M", datetime.now()-1)
        self.create_song(2, datetime.now(), "dean", "rock", "M", datetime.now()-1)
        self.create_song(3, datetime.now(), "allan", "rock", "M", datetime.now()-1)
        self.create_song(4, datetime.now(), "mike", "rock", "M", datetime.now()-1)


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("employees-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Employees.objects.all()
        serialized = EmployeeSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
# Create your tests here.
