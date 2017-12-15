from django.urls import reverse
from django.test import TestCase, Client, RequestFactory
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
import datetime

from employees.models import Employee
from habitat.models import Habitat
from squad.models import Squad, SquadEmployee
from squad.serializers import SquadSerializer, SquadEmployeeSerializer

def create_squad_serializer(data, url, many = False):
    request = APIRequestFactory().get(url)
    serializer = SquadSerializer(data, many = many, context = {'request': request})
    return serializer

def create_squademployee_serializer(data, url, many = False):
    request = APIRequestFactory().get(url)
    serializer = SquadSerializer(data, many = many, context = {'request': request})
    return serializer

class SquadTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.squad = Squad.objects.create(
            name="TestSquad"
        )
        self.squad_json = {
            "name": "TestSquad"
        }
        self.url_with_id = reverse('squad-detail', args=[self.squad.id])
        self.url_absolute_with_id = 'http://testserver/squads/' + str(self.squad.id) + '/'

    """
    Tests for SquadSerializer
    """
    def test_squad_serializer_expected_fields(self):
        """
        The serializer should only expect and accept the fields that have been set
        """
        serializer = create_squad_serializer(self.squad, '')
        self.assertSetEqual(set(serializer.data.keys()), {'id', 'name'})
    
    def test_squad_serializer_id_name_field_content(self):
        """
        The name field of a squad should contain a name
        """
        serializer = create_squad_serializer(self.squad, '')
        self.assertEqual(serializer.data['id'], self.squad.id)
    
    def test_squad_serializer_name_field_content(self):
        """
        The name field of a squad should contain a name
        """
        serializer = create_squad_serializer(self.squad, '')
        self.assertEqual(serializer.data['name'], self.squad.name)

    def test_squad_serializer_returns_empty_when_no_squads(self):
        """
        The serializer should return [] when no objects are given
        """
        squad = Squad.objects.none()
        serialzer = create_squad_serializer(squad, '/', many = True)
        self.assertEqual(serialzer.data, [])

    """
    Tests for the /squads/<id>/ path
    """
    def test_get_squad_returns_200_when_found(self):
        """
        A GET request on /squads/<id>/ should return a squad
        """
        serializer = create_squad_serializer(self.squad, self.url_with_id)
        response = self.client.get(self.url_with_id, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
    def test_get_squad_returns_404_when_not_found(self):
        """
        A GET request on /squads/<id>/ should return a 404 error when the squad doesn't exist
        """
        url = reverse('squad-detail', args=[-2])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_post_squad_returns_405(self):
        """
        A POST request on /squads/<id>/ should not be possible
        """
        response = self.client.post(self.url_with_id, self.squad_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_put_squad_returns_200_when_updated(self):
        """
        A PUT request on /squads/<id>/ should return an updated squad
        """
        response = self.client.put(self.url_with_id, self.squad_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_squad_returns_404_when_not_found(self):
        """
        A PUT request on /squads/<id>/ should return a 404 when using an invalid id
        """
        url = reverse('squad-detail', args=[999])
        response = self.client.put(url, self.squad_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_put_squad_returns_400_when_bad_format(self):
        """
        A PUT request on /squads/<id>/ should return an updated squad
        """
        squad_json = {'title': 'TestTitle'}
        url = reverse('squad-detail', args=[self.squad.id])
        response = self.client.put(url, squad_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)   
        
    def test_delete_squad_returns_204_when_deleting(self):
        """
        A DELETE request on /squads/<id>/ should delete a squad
        """
        response = self.client.delete(self.url_with_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_delete_squad_returns_404_when_not_found(self):
        """
        A DELETE request on /squads/<id>/ should return 404 when deleting unexisting squad
        """
        url = reverse('employee-detail', args=[999])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_patch_squad_returns_200_when_updated(self):
        """
        A PATCH request on /squads/<id>/ should return an updated squad
        """
        response = self.client.patch(self.url_with_id, self.squad_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_squad_returns_400_when_bad_format(self):
        """
        A PATCH request on /squads/<id>/ should return an updated squad
        """
        url = reverse('squad-detail', args=[self.squad.id])
        response = self.client.patch(url, '{}', format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_patch_squad_returns_404_when_not_found(self):
        """
        A PATCH request on /squads/<id>/ should return 404 when not found
        """
        url = reverse('squad-detail', args=[999])
        response = self.client.patch(url, self.squad_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    Tests for the /squads/ path
    """
    def test_get_all_squad_returns_200_when_found(self):
        """
        A GET request on /squads/ should return an array of squads
        """
        url = reverse('squad-list')
        squads = Squad.objects.all()
        serializer = create_squad_serializer(squads, url, many=True)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
    def test_get_all_squad_returns_200_when_non_found(self):
        """
        A GET request on /squads/ should still work with no results and return an empty array
        """
        url = reverse('squad-list')
        squads = Squad.objects.none()
        response = self.client.get('/squads/')
        serializer = create_squad_serializer(squads, url, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_all_squad_returns_201_when_correct_format(self):
        """
        A POST request on /squads/ should create a new squad
        """
        response = self.client.post('/squads/', self.squad_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)

    def test_post_all_squad_returns_400_when_bad_format(self):
        """
        A POST request on /squads/ using the wrong format should return a 400 error
        """
        data = {'title': 'NewSquad'}
        response = self.client.post('/squads/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_all_squad_returns_405(self):
        """
        A PUT request on /squads/ should not be possible
        """
        url = reverse('squad-list')
        response = self.client.put(url, self.squad_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_patch_all_squad_returns_405(self):
        """
        A PATCH request on /squads/ should not be possible
        """
        url = reverse('squad-list')
        response = self.client.patch(url, self.squad_json, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_delete_all_squad_returns_405(self):
        """
        A DELETE request on /squads/ should not be possible
        """
        url = reverse('squad-list')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
