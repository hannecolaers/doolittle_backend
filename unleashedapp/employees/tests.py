from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.utils.datetime_safe import datetime
from rest_framework import status
import datetime

from rest_framework.test import APIClient, APIRequestFactory

from employees.models import Employee
from employees.serializers import EmployeeSerializer
from habitat.models import Habitat


def create_serializer(data, url, many=False):
    request = RequestFactory().get(url)
    serializer = EmployeeSerializer(data, many=many, context={'request': request})
    return serializer


class EmployeeTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.habitat = Habitat.objects.create(
            name="habitat1"
        )
        self.employee = Employee.objects.create(
            first_name='testVoornaam',
            last_name='testAchternaam',
            function='testFunctie',
            start_date=datetime.date.today(),
            visible_site=True,
            habitat=self.habitat
        )
        self.employee_json = {
            "first_name": "test",
            "last_name": "test",
            "function": "testFunctie",
            "start_date": "2017-12-13",
            "visible_site": False,
            "habitat": {
                "name": "habitat1"
            }
        }
        self.url_with_id = reverse('employee-detail', args=[self.employee.id])
        self.url_absolute_with_id = 'http://testserver/employees/' + str(self.employee.id) + '/'

    """ 
        Test serializer 
    """

    def test_employee_serializer_expected_fields(self):
        """
            Ensure the serializer contains the expected fields
        """
        serializer = create_serializer(self.employee, '/test')
        self.assertSetEqual(set(serializer.data.keys()),
                            {'id', 'first_name', 'last_name', 'function', 'start_date',
                             'end_date', 'visible_site', 'habitat'}
                            )

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
        serializer = create_serializer(self.employee, self.url_with_id)
        response = self.client.get(self.url_with_id, format="json")
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
            Ensure we can post an employee and ensure an id is added
        """
        response = self.client.post('/employees/', self.employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)

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
            "habitat": {
                "name": "habitat1"
            }
        }
        response = self.client.post('/employees/', employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_missing_field(self):
        """
            Ensure a POST request with an employee with a missing field returns 400 bad request
        """
        employee_json = {
            'last_name': 'testAchternaam',
            'function': 'testFunctie',
            'start_date': '2017-12-08',
            'visible_site': '1',
            "habitat": {
                "name": "habitat1"
            }
        }
        response = self.client.post('/employees/', employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_invalid_habitat_fk(self):
        """
            Ensure a POST request with an invalid foreign key to a habitat returns 400 bad request
        """
        employee_json = {
            "first_name": "test",
            "last_name": "test",
            "function": "testFunctie",
            "start_date": "2017-12-13",
            "visible_site": False,
            "habitat": {
                "name": "x"
            }
        }
        response = self.client.post('/employees/', employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_to_id(self):
        """
            Ensure a post to employess/id/ return 405 method not allowed
        """
        response = self.client.post(self.url_with_id, self.employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_employee_update(self):
        """
            Ensure an employee can be updated with a PUT request
        """
        response = self.client.put(self.url_with_id, self.employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_employee_change_habitat(self):
        """
            Ensure an employee can be updated with a PUT request
        """
        response = self.client.put(self.url_with_id, self.employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_invalid_id(self):
        """
            Ensure that a PUT request with an invalid id in url returns a 404 not found
        """
        url = reverse('employee-detail', args=['x'])
        response = self.client.put(url, self.employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_nonexisting_id(self):
        """
            Ensure that a PUT request with a non existing id in url returns a 404 not found
        """
        url = reverse('employee-detail', args=[999])
        response = self.client.put(url, self.employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_negative_id(self):
        """
            Ensure that a PUT request with a negative id in url returns a 404 not found
        """
        url = reverse('employee-detail', args=[-10])
        response = self.client.put(url, self.employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_empty_body(self):
        """
            Ensure that a PUT request with an empty body returns a 400 bad request
        """
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.put(url, '{}', format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_invalid(self):
        """
            Ensure that a PUT request with invalid data returns a 400 bad request
        """
        employee_json = {
            'first_name': 'testVoornaam',
            'last_name': 'testAchternaam',
            'function': 'testFunctie',
            'start_date': 'xx',
            'visible_site': '1',
            'habitat': 'testHabitat'
        }
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.put(url, employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_missing_required_field(self):
        """
            Ensure that a PUT request with a missing required field returns a 400 bad request
        """
        employee_json = {
            'last_name': 'testAchternaam',
            'function': 'testFunctie',
            'start_date': '2017-2-2',
            'visible_site': '1',
            'habitat': 'testHabitat'
        }
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.put(url, employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_employee_list(self):
        """
            Ensure a PUT request to /employees/ returns a 405 not allowed
        """
        url = reverse('employee-list')
        response = self.client.put(url, self.employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_employee_update(self):
        """
            Ensure an employee can be updated with a PATCH request
        """
        response = self.client.patch(self.url_with_id, self.employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_employee_update_partial(self):
        """
            Ensure a certain field of an employee can be updated with a PATCH request
        """
        employee_json = {
            'last_name': 'testAchternaam',
        }
        response = self.client.patch(self.url_with_id, employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_invalid_id(self):
        """
            Ensure that a PATCH request with an invalid id in url returns a 404 not found
        """
        url = reverse('employee-detail', args=['x'])
        response = self.client.patch(url, self.employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_nonexisting_id(self):
        """
            Ensure that a PATCH request with a non existing id in url returns a 404 not found
        """
        url = reverse('employee-detail', args=[999])
        response = self.client.patch(url, self.employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_negative_id(self):
        """
            Ensure that a PATCH request with a negative id in url returns a 404 not found
        """
        url = reverse('employee-detail', args=[-10])
        response = self.client.patch(url, self.employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_empty_body(self):
        """
            Ensure that a PATCH request with an empty body returns a 400 bad request
        """
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.patch(url, '{}', format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_invalid(self):
        """
            Ensure that a PATCH request with invalid data returns a 400 bad request
        """
        employee_json = {
            'start_date': 'xx'
        }
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.patch(url, employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_employee_list(self):
        """
            Ensure a PATCH request to /employees/ returns a 405 not allowed
        """
        url = reverse('employee-list')
        response = self.client.patch(url, self.employee_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_employee(self):
        """
            Ensure a DELETE request of a valid employee id returns 200 OK
        """
        response = self.client.delete(self.url_with_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_id(self):
        """
            Ensure that a DELETE request with an invalid id in url returns a 404 not found
        """
        url = reverse('employee-detail', args=['x'])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_nonexisting_id(self):
        """
            Ensure that a DELETE request with a non existing id in url returns a 404 not found
        """
        url = reverse('employee-detail', args=[999])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_negative_id(self):
        """
            Ensure that a DELETE request with a negative id in url returns a 404 not found
        """
        url = reverse('employee-detail', args=[-10])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_employee_list(self):
        """
            Ensure a DELETE request to /employees/ returns a 405 not allowed
        """
        url = reverse('employee-list')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
