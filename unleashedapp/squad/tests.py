from squad.models import Squad
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class SquadTestCase(APITestCase):
    """
    Tests for the /squads/<id> path
    """
    def test_get_squad_returns_200_when_found(self):
        """
        A GET request on /squads/<id> should return a squad
        """
        response = self.client.post('/squads/', {'name': 'FirstSquad'}, format='json')
        response = self.client.get('/squads/4/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 4, 'name': 'FirstSquad'})
        
    def test_get_squad_returns_404_when_not_found(self):
        """
        A GET request on /squads/<id> should return a 404 error when the squad doesn't exist
        """
        response = self.client.get('/squads/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_post_squad_returns_405(self):
        """
        A POST request on /squads/<id> should not be possible
        """
        data = {'name': 'NewSquad'}
        response = self.client.post('/squads/4/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_put_squad_returns_200_when_updated(self):
        """
        A PUT request on /squads/<id> should return an updated squad
        """
        response = self.client.post('/squads/', {'name': 'OldlyNamedSquad'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'id': 8, 'name': 'OldlyNamedSquad'})
        response = self.client.put('/squads/8/', {'name': 'NewlyNamedSquad'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 8, 'name': 'NewlyNamedSquad'})
        
    def test_put_squad_returns_404_when_not_found(self):
        """
        A PUT request on /squads/<id> should return a 404 when using an invalid id
        """
        response = self.client.put('/squads/957/', {'name': 'NewlyNamedSquad'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_delete_squad_returns_204_when_deleting(self):
        """
        A DELETE request on /squads/<id> should delete a squad
        """
        response = self.client.post('/squads/', {'name': 'DeletableSquad'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'id': 1, 'name': 'DeletableSquad'})
        response = self.client.delete('/squads/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_delete_squad_returns_404_when_not_found(self):
        """
        A DELETE request on /squads/<id> should return 404 when deleting unexisting squad
        """
        response = self.client.delete('/squads/989/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_patch_squad_returns_200_when_updated(self):
        """
        A PATCH request on /squads/<id> should return an updated squad
        """
        response = self.client.post('/squads/', {'name': 'OldlyPatchedSquad'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'id': 5, 'name': 'OldlyPatchedSquad'})
        response = self.client.patch('/squads/5/', {'name': 'NewlyPatchedSquad'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 5, 'name': 'NewlyPatchedSquad'})
        
    def test_patch_squad_returns_404_when_not_found(self):
        """
        A PATCH request on /squads/<id> should return 404 when not found
        """
        response = self.client.patch('/squads/934/', {'name': 'NeverBeFoundSquad'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    """
    Tests for the /squads/ path
    """
    def test_get_all_squad_returns_200_when_found(self):
        """
        A GET request on /squads/ should return an array of squads
        """
        response = self.client.post('/squads/', {'name': 'DefaultSquad'}, format='json')
        response = self.client.post('/squads/', {'name': 'FancySquad'}, format='json')
        response = self.client.get('/squads/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'id': 2, 'name': 'DefaultSquad'}, {'id': 3, 'name': 'FancySquad'}])
        
    def test_get_all_squad_returns_200_when_non_found(self):
        """
        A GET request on /squads/ should still work with no results and return an empty array
        """
        response = self.client.get('/squads/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_post_all_squad_returns_201_when_correct_format(self):
        """
        A POST request on /squads/ should create a new squad
        """
        data = {'name': 'NewSquad'}
        response = self.client.post('/squads/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Squad.objects.count(), 1)
        self.assertEqual(Squad.objects.get().name, 'NewSquad')

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
        response = self.client.put('/squads/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_patch_all_squad_returns_405(self):
        """
        A PATCH request on /squads/ should not be possible
        """
        response = self.client.patch('/squads/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_delete_all_squad_returns_405(self):
        """
        A DELETE request on /squads/ should not be possible
        """
        response = self.client.delete('/squads/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)