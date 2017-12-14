from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from habitat.models import Habitat
from habitat.serializers import HabitatSerializer

def create_serializer(data, url, many = False):
    request = APIRequestFactory().get(url)
    serializer = HabitatSerializer(data, many = many, context = {'request': request})
    return serializer

class HabitatTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    """
    Tests for HabitatSerializer
    """
    def test_habitat_serializer_expected_fields(self):
        """
        The serializer should only expect and accept the fields that have been set
        """
        self.habtiat = Habitat.objects.create(name = "TestHabitat")
        serializer = create_serializer(self.habtiat, '')
        self.assertSetEqual(set(serializer.data.keys()), {'id', 'name'})
    
    def test_habitat_serializer_id_name_field_content(self):
        """
        The name field of a habitat should contain a name
        """
        self.habtiat = Habitat.objects.create(name = "TestHabitat")
        serializer = create_serializer(self.habtiat, '')
        self.assertEqual(serializer.data['id'], self.habtiat.id)
    
    def test_habitat_serializer_name_field_content(self):
        """
        The name field of a habitat should contain a name
        """
        self.habtiat = Habitat.objects.create(name = "TestHabitat")
        serializer = create_serializer(self.habtiat, '')
        self.assertEqual(serializer.data['name'], self.habtiat.name)

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
        response = self.client.post('/habitats/', {'name': 'FirstHabitat'}, format='json')
        response = self.client.get('/habitats/4/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 4, 'name': 'FirstHabitat'})
        
    def test_get_habitat_returns_404_when_not_found(self):
        """
        A GET request on /habitats/<id>/ should return a 404 error when the habitat doesn't exist
        """
        response = self.client.get('/habitats/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_post_habitat_returns_405(self):
        """
        A POST request on /habitats/<id>/ should not be possible
        """
        data = {'name': 'NewHabitat'}
        response = self.client.post('/habitats/4/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_put_habitat_returns_200_when_updated(self):
        """
        A PUT request on /habitats/<id>/ should return an updated habitat
        """
        response = self.client.post('/habitats/', {'name': 'OldlyNamedHabitat'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'id': 11, 'name': 'OldlyNamedHabitat'})
        response = self.client.put('/habitats/11/', {'name': 'NewlyNamedHabitat'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 11, 'name': 'NewlyNamedHabitat'})
        
    def test_put_habitat_returns_404_when_not_found(self):
        """
        A PUT request on /habitats/<id>/ should return a 404 when using an invalid id
        """
        response = self.client.put('/habitats/957/', {'name': 'NewlyNamedHabitat'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_put_habitat_returns_400_when_bad_format(self):
        """
        A PUT request on /habitats/<id>/ should return an updated habitat
        """
        response = self.client.post('/habitats/', {'name': 'OldlyNamedExtraHabitat'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'id': 12, 'name': 'OldlyNamedExtraHabitat'})
        response = self.client.put('/habitats/12/', {'title': 'NewlyNamedExtraHabitat'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_delete_habitat_returns_204_when_deleting(self):
        """
        A DELETE request on /habitats/<id>/ should delete a habitat
        """
        response = self.client.post('/habitats/', {'name': 'DeletableHabitat'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'id': 1, 'name': 'DeletableHabitat'})
        response = self.client.delete('/habitats/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_delete_habitat_returns_404_when_not_found(self):
        """
        A DELETE request on /habitats/<id>/ should return 404 when deleting unexisting habitat
        """
        response = self.client.delete('/habitats/989/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_patch_habitat_returns_200_when_updated(self):
        """
        A PATCH request on /habitats/<id>/ should return an updated habitat
        """
        response = self.client.post('/habitats/', {'name': 'OldlyPatchedHabitat'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'id': 8, 'name': 'OldlyPatchedHabitat'})
        response = self.client.patch('/habitats/8/', {'name': 'NewlyPatchedHabitat'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 8, 'name': 'NewlyPatchedHabitat'})
        
    def test_patch_habitat_returns_400_when_bad_format(self):
        """
        A PATCH request on /habitats/<id>/ should return an updated habitat
        """
        response = self.client.post('/habitats/', {'name': 'BrokenPatchHabitat'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'id': 9, 'name': 'BrokenPatchHabitat'})
        response = self.client.patch('/habitats/9/', {'name': None}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_patch_habitat_returns_404_when_not_found(self):
        """
        A PATCH request on /habitats/<id>/ should return 404 when not found
        """
        response = self.client.patch('/habitats/934/', {'name': 'NeverBeFoundHabitat'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    """
    Tests for the /habitats/ path
    """
    def test_get_all_habitat_returns_200_when_found(self):
        """
        A GET request on /habitats/ should return an array of habitats
        """
        response = self.client.post('/habitats/', {'name': 'DefaultHabitat'}, format='json')
        response = self.client.post('/habitats/', {'name': 'FancyHabitat'}, format='json')
        response = self.client.get('/habitats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'id': 2, 'name': 'DefaultHabitat'}, {'id': 3, 'name': 'FancyHabitat'}])
        
    def test_get_all_habitat_returns_200_when_non_found(self):
        """
        A GET request on /habitats/ should still work with no results and return an empty array
        """
        response = self.client.get('/habitats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_post_all_habitat_returns_201_when_correct_format(self):
        """
        A POST request on /habitats/ should create a new habitat
        """
        data = {'name': 'NewHabitat'}
        response = self.client.post('/habitats/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habitat.objects.count(), 1)
        self.assertEqual(Habitat.objects.get().name, 'NewHabitat')

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
        response = self.client.put('/habitats/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_patch_all_habitat_returns_405(self):
        """
        A PATCH request on /habitats/ should not be possible
        """
        response = self.client.patch('/habitats/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_delete_all_habitat_returns_405(self):
        """
        A DELETE request on /habitats/ should not be possible
        """
        response = self.client.delete('/habitats/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

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
        self.assertEqual(response.status_code, status.HTTP_200_OK)