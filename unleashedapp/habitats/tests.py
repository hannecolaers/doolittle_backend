from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory

from habitats.models import Habitat
from habitats.serializers import HabitatSerializer
from django.contrib.auth.models import User


def create_serializer(data, url, many = False):
    request = APIRequestFactory().get(url)
    serializer = HabitatSerializer(data, many=many, context={'request': request})
    return serializer


class HabitatTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create(username='test')
        self.client.force_authenticate(user=user)
        self.habitat = Habitat.objects.create(
            name="TestHabitat"
        )
        self.habitat_json = {
            "name": "TestHabitat"
        }
        self.url_with_id = reverse('habitat-detail', args=[self.habitat.id])
        self.url_absolute_with_id = 'http://testserver/habitats/' + str(self.habitat.id) + '/'


    """
    Tests for HabitatSerializer
    """
    def test_habitat_serializer_expected_fields(self):
        """
        The serializer should only expect and accept the fields that have been set
        """
        serializer = create_serializer(self.habitat, '')
        self.assertSetEqual(set(serializer.data.keys()), {'id', 'name'})
    
    def test_habitat_serializer_id_name_field_content(self):
        """
        The name field of a habitat should contain a name
        """
        serializer = create_serializer(self.habitat, '')
        self.assertEqual(serializer.data['id'], self.habitat.id)
    
    def test_habitat_serializer_name_field_content(self):
        """
        The name field of a habitat should contain a name
        """
        serializer = create_serializer(self.habitat, '')
        self.assertEqual(serializer.data['name'], self.habitat.name)

    def test_habitat_serializer_returns_empty_when_no_habitats(self):
        """
        The serializer should return [] when no objects are given
        """
        habitat = Habitat.objects.none()
        serialzer = create_serializer(habitat, '/', many = True)
        self.assertEqual(serialzer.data, [])

    """
    Tests for the /habitats/<id>/ path
    """
    def test_get_habitat_returns_200_when_found(self):
        """
        A GET request on /habitats/<id>/ should return a habitat
        """
        serializer = create_serializer(self.habitat, self.url_with_id)
        response = self.client.get(self.url_with_id, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
    def test_get_habitat_returns_404_when_not_found(self):
        """
        A GET request on /habitats/<id>/ should return a 404 error when the habitat doesn't exist
        """
        url = reverse('habitat-detail', args=[-2])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_post_habitat_returns_405(self):
        """
        A POST request on /habitats/<id>/ should not be possible
        """
        response = self.client.post(self.url_with_id, self.habitat_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_put_habitat_returns_200_when_updated(self):
        """
        A PUT request on /habitats/<id>/ should return an updated habitat
        """
        response = self.client.put(self.url_with_id, self.habitat_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_habitat_returns_404_when_not_found(self):
        """
        A PUT request on /habitats/<id>/ should return a 404 when using an invalid id
        """
        url = reverse('habitat-detail', args=[999])
        response = self.client.put(url, self.habitat_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_put_habitat_returns_400_when_bad_format(self):
        """
        A PUT request on /habitats/<id>/ should return an updated habitat
        """
        habitat_json = {'title': 'TestTitle'}
        url = reverse('habitat-detail', args=[self.habitat.id])
        response = self.client.put(url, habitat_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)   
        
    def test_delete_habitat_returns_204_when_deleting(self):
        """
        A DELETE request on /habitats/<id>/ should delete a habitat
        """
        response = self.client.delete(self.url_with_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_delete_habitat_returns_404_when_not_found(self):
        """
        A DELETE request on /habitats/<id>/ should return 404 when deleting unexisting habitat
        """
        url = reverse('employee-detail', args=[999])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_patch_habitat_returns_200_when_updated(self):
        """
        A PATCH request on /habitats/<id>/ should return an updated habitat
        """
        response = self.client.patch(self.url_with_id, self.habitat_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_habitat_returns_400_when_bad_format(self):
        """
        A PATCH request on /habitats/<id>/ should return an updated habitat
        """
        url = reverse('habitat-detail', args=[self.habitat.id])
        response = self.client.patch(url, '{}', format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_patch_habitat_returns_404_when_not_found(self):
        """
        A PATCH request on /habitats/<id>/ should return 404 when not found
        """
        url = reverse('habitat-detail', args=[999])
        response = self.client.patch(url, self.habitat_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    Tests for the /habitats/ path
    """
    def test_get_all_habitat_returns_200_when_found(self):
        """
        A GET request on /habitats/ should return an array of habitats
        """
        url = reverse('habitat-list')
        habitats = Habitat.objects.all()
        serializer = create_serializer(habitats, url, many=True)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
    def test_get_all_habitat_returns_200_when_non_found(self):
        """
        A GET request on /habitats/ should still work with no results and return an empty array
        """
        url = reverse('habitat-list')
        habitats = Habitat.objects.none()
        response = self.client.get('/habitats/')
        serializer = create_serializer(habitats, url, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_all_habitat_returns_201_when_correct_format(self):
        """
        A POST request on /habitats/ should create a new habitat
        """
        response = self.client.post('/habitats/', self.habitat_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)

    def test_post_all_habitat_returns_400_when_bad_format(self):
        """
        A POST request on /habitats/ using the wrong format should return a 400 error
        """
        data = {'title': 'NewHabitat'}
        response = self.client.post('/habitats/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_all_habitat_returns_405(self):
        """
        A PUT request on /habitats/ should not be possible
        """
        url = reverse('habitat-list')
        response = self.client.put(url, self.habitat_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_patch_all_habitat_returns_405(self):
        """
        A PATCH request on /habitats/ should not be possible
        """
        url = reverse('habitat-list')
        response = self.client.patch(url, self.habitat_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_delete_all_habitat_returns_405(self):
        """
        A DELETE request on /habitats/ should not be possible
        """
        url = reverse('habitat-list')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
'''
    """
    Tests for the /habitats/<id>/employees/ path
    """
    def test_get_habitat_employees_returns_20_when_not_found(self):
        """
        A GET request on /habitats/<id>/employees/ should return a 200 error
        when the habitat doesn't exist, because you request the users in that habitat
        """
        response = self.client.get('/habitats/999/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_post_habitat_employees_returns_405(self):
        """
        A POST request on /habitats/<id>/employees/ should not be possible
        """
        data = {'name': 'NewHabitat'}
        response = self.client.post('/habitats/1/employees/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_put_habitat_employees_returns_405(self):
        """
        A PUT request on /habitats/<id>/employees/ should not be possible
        """
        response = self.client.put('/habitats/1/employees/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_patch_habitat_employees_returns_405(self):
        """
        A PATCH request on /habitats/<id>/employees/ should not be possible
        """
        response = self.client.patch('/habitats/1/employees/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_delete_habitat_employees_returns_405(self):
        """
        A DELETE request on /habitats/<id>/employees/ should not be possible
        """
        response = self.client.delete('/habitats/1/employees/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_habitat_returns_200_when_found(self):
        """
        A GET request on /habitats/<id>/employees/ should return a list of employees
        """
        response = self.client.post('/habitats/', {'name': 'Employbitat'}, format='json')
        response = self.client.post('/employees/', {"first_name": "Firstname", "last_name": "Lastname", "function": "Person", "start_date": "2017-12-13", "visible_site": False, "habitat": 4}, format='json')
        response = self.client.post('/employees/', {"first_name": "Newname", "last_name": "Oldname", "function": "Developer", "start_date": "2017-12-13", "visible_site": False, "habitat": 4}, format='json')
        response = self.client.get('/habitats/4/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK) '''