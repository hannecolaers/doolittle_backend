from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.utils.datetime_safe import datetime
from rest_framework import status
import datetime

from rest_framework.test import APIClient, APIRequestFactory

from employees.models import Employee
from employees.serializers import EmployeeSerializer


def create_serializer(data, url, many=False):
    request = RequestFactory().get(url)
    serializer = EmployeeSerializer(data, many=many, context={'request': request})
    return serializer


class EmployeeTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.employee = Employee.objects.create(
            first_name='testVoornaam',
            last_name='testAchternaam',
            function='testFunctie',
            start_date=datetime.date.today(),
            visible_site=True,
            habitat='testHabitat'
        )

    """ 
        Test serializer 
    """

    def test_employee_serializer_expected_fields(self):
        """
            Ensure the serializer contains the expected fields
        """
        serializer = create_serializer(self.employee, '/test')
        self.assertEquals(set(serializer.data.keys()),
                          {'url', 'id', 'first_name', 'last_name', 'function', 'start_date',
                           'end_date', 'visible_site', 'habitat'}
                          )

    def test_serializer_url_field_content(self):
        """
            Ensure that the url field contains the expected data
        """
        serializer = create_serializer(self.employee, '')
        url = 'http://testserver/employees/' + str(self.employee.id) + '/'
        self.assertEqual(serializer.data['url'], url)

    def test_serializer_id_field_content(self):
        """
            Ensure that the id field contains the expected data
        """
        serializer = create_serializer(self.employee, '')
        self.assertEqual(serializer.data['id'], self.employee.id)

    def test_serializer_first_name_field_content(self):
        """
            Ensure that the first_name field contains the expected data
        """
        serializer = create_serializer(self.employee, '')
        self.assertEqual(serializer.data['first_name'], self.employee.first_name)

    def test_serializer_last_name_field_content(self):
        """
            Ensure that the last_name field contains the expected data
        """
        serializer = create_serializer(self.employee, '')
        self.assertEqual(serializer.data['last_name'], self.employee.last_name)

    def test_serializer_function_field_content(self):
        """
            Ensure that the function field contains the expected data
        """
        serializer = create_serializer(self.employee, '')
        self.assertEqual(serializer.data['function'], self.employee.function)

    def test_serializer_start_date_field_content(self):
        """
            Ensure that the start_date field contains the expected data
        """
        serializer = create_serializer(self.employee, '')
        self.assertEqual(serializer.data['start_date'], str(self.employee.start_date))

    def test_serializer_end_date_field_content(self):
        """
            Ensure that the end_date field contains the expected data
        """
        serializer = create_serializer(self.employee, '')
        self.assertEqual(serializer.data['end_date'], self.employee.end_date)

    def test_serializer_visible_site_field_content(self):
        """
            Ensure that the visible_site field contains the expected data
        """
        serializer = create_serializer(self.employee, '')
        self.assertEqual(serializer.data['visible_site'], self.employee.visible_site)

    def test_serializer_habitat_field_content(self):
        """
            Ensure that the habitat field contains the expected data
        """
        serializer = create_serializer(self.employee, '')
        self.assertEqual(serializer.data['habitat'], self.employee.habitat)

    def test_serializer_empty_object(self):
        """
            Ensure that the serializer returns [] if the object is empty
        """
        emptyqueryset = Employee.objects.none()
        serializer = create_serializer(emptyqueryset, '/', many=True)
        self.assertEqual(serializer.data, [])

    """ 
        tests rest api 
    """

    def test_get_all_employees(self):
        """
            Ensure we can get a list of all the employees
        """
        url = reverse('employee-list')
        employees = Employee.objects.all()
        serializer = create_serializer(employees, url, many=True)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_employee_by_id(self):
        """
            Ensure we can get an employee by id
        """
        url = reverse('employee-detail', args=[self.employee.id])
        serializer = create_serializer(self.employee, url)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_employee_by_unknown_id(self):
        """
            Ensure an unknown employee id returns a 404 not found
        """
        url = reverse('employee-detail', args=[-2])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_employee(self):
        """
            Ensure we can post an employee
        """
        employee_json = {
            'first_name': 'testVoornaam',
            'last_name': 'testAchternaam',
            'function': 'testFunctie',
            'start_date': '2017-12-08',
            'visible_site': '1',
            'habitat': 'testHabitat'
        }
        response = self.client.post('/employees/', employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_date(self):
        """
            Ensure an employee with an invalid date returns 400 bad request
        """
        employee_json = {
            'first_name': 'testVoornaam',
            'last_name': 'testAchternaam',
            'function': 'testFunctie',
            'start_date': 'xx',
            'visible_site': '1',
            'habitat': 'testHabitat'
        }
        response = self.client.post('/employees/', employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_missing_field(self):
        """
            Ensure an employee with a missing field returns 400 bad request
        """
        employee_json = {
            'last_name': 'testAchternaam',
            'function': 'testFunctie',
            'start_date': 'xx',
            'visible_site': '1',
            'habitat': 'testHabitat'
        }
        response = self.client.post('/employees/', employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # TODO
    # def test_post_invalid_habitat_fk(self):

    def test_post_to_id(self):
        """
            Ensure a post to employess/id/ return 405 method not allowed
        """
        employee_json = {
            'last_name': 'testAchternaam',
            'function': 'testFunctie',
            'start_date': 'xx',
            'visible_site': '1',
            'habitat': 'testHabitat'
        }
        response = self.client.post('/employees/1/', employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
