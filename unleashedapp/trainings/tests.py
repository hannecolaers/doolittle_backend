from django.test import TestCase, Client
from rest_framework import status
import json

import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SquadTestCase(TestCase):
    def setUp(self):
        # Authenticate with Google
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        self.gclient = gspread.authorize(creds)
        # Create a new, empty spreadsheet and worksheet
        self.sh = self.gclient.open_by_key('1jEZR1uaEylQ05AohVvRpdQSWGOl7nDQE4oDtTWVAGkw')
        self.ws = self.sh.worksheet('TestSheet')
        self.ws.resize(rows=1, cols=11)
        self.training_json = {
            "date": "1/1/2018",
            "days": 1,
            "firstname": "Testuser",
            "lastname": "Testname",
            "team": "Care",
            "training": "Django",
            "company": "PXL",
            "city": "Hasselt",
            "cost": 1.8,
            "invoice": "Yep",
            "info": "Nope"
        }
        self.training_json_partial = {
            "date": "1/1/2018",
            "days": 1,
            "firstname": "Testuser",
            "lastname": "Franssen",
            "team": "Careful",
            "training": "REST Framework"
        }

    """
    Tests for the /trainings/<id>/ path
    """
    '''     def test_get_training_returns_200_when_found(self):
        """
        A GET request on /trainings/<id>/ should return an array of trainings
        """
        self.ws.append_row(["1/1/2018",1,"Testuser","Testname","Care","Text","PXL","Hasselt",1.8,"Yep","Nope"])
        response = self.client.get('/trainings/2/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    '''
    def test_get_training_returns_404_when_requesting_1(self):
        """
        A GET request on /trainings/<id>/ should return an array of trainings
        """
        response = self.client.get('/trainings/1/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_get_training_returns_404_when_not_found(self):
        """
        A GET request on /trainings/<id>/ should return an array of trainings
        """
        response = self.client.get('/trainings/999/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_post_training_returns_405(self):
        """
        A GET request on /trainings/<id>/ should return an array of trainings
        """
        response = self.client.post('/trainings/2/?sheet=TestSheet', json.dumps(self.training_json), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_training_returns_200_when_updated(self):
        """
        A GET request on /trainings/<id>/ should return an array of trainings
        """
        self.ws.append_row(["1/1/2018",1,"Testuser","Testname","Care","Text","PXL","Hasselt",1.8,"Yep","Nope"])
        response = self.client.put('/trainings/2/?sheet=TestSheet', json.dumps(self.training_json_partial), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_put_training_returns_404_when_requesting_1(self):
        """
        A GET request on /trainings/<id>/ should return an array of trainings
        """
        self.ws.append_row(["1/1/2018",1,"Testuser","Testname","Care","Text","PXL","Hasselt",1.8,"Yep","Nope"])
        response = self.client.put('/trainings/1/?sheet=TestSheet', json.dumps(self.training_json_partial), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_training_returns_404_when_not_found(self):
        """
        A GET request on /trainings/<id>/ should return an array of trainings
        """
        self.ws.append_row(["1/1/2018",1,"Testuser","Testname","Care","Text","PXL","Hasselt",1.8,"Yep","Nope"])
        response = self.client.put('/trainings/999/?sheet=TestSheet', json.dumps(self.training_json_partial), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_training_returns_400_when_bad_format(self):
        """
        A POST request on /trainings/<id>/ using the wrong format should return a 400 error
        """
        self.ws.append_row(["1/1/2018",1,"Testuser","Testname","Care","Text","PXL","Hasselt",1.8,"Yep","Nope"])
        data = {'title': 'Newtraining'}
        response = self.client.put('/trainings/2/?sheet=TestSheet', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_training_returns_204_when_deleting(self):
        """
        A DELETE request on /trainings/<id>/ should delete a training
        """
        self.ws.append_row(["1/1/2018",1,"Testuser","Testname","Care","Text","PXL","Hasselt",1.8,"Yep","Nope"])
        response = self.client.delete('/trainings/2/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_delete_training_returns_404_when_not_found(self):
        """
        A DELETE request on /trainings/<id>/ should return 404 when deleting unexisting training
        """
        response = self.client.delete('/trainings/999/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    Tests for the /trainings/ path
    """
    def test_get_all_training_returns_200_when_found(self):
        """
        A GET request on /trainings/ should return an array of trainings
        """
        self.ws.append_row(["1/1/2018",1,"Testuser","Testname","Care","Text","PXL","Hasselt",1.8,"Yep","Nope"])
        response = self.client.get('/trainings/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_training_returns_200_when_non_found(self):
        """
        A GET request on /trainings/ should still work with no results and return an empty array
        """
        response = self.client.get('/trainings/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_all_training_returns_201_when_correct_format(self):
        """
        A POST request on /trainings/ should create a new training
        """
        response = self.client.post('/trainings/?sheet=TestSheet', json.dumps(self.training_json), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_all_training_returns_400_when_bad_format(self):
        """
        A POST request on /trainings/ using the wrong format should return a 400 error
        """
        data = {'title': 'Newtraining'}
        response = self.client.post('/trainings/?sheet=TestSheet', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_all_training_returns_405(self):
        """
        A PUT request on /trainings/ should not be possible
        """
        response = self.client.put('/trainings/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_all_training_returns_405(self):
        """
        A PATCH request on /trainings/ should not be possible
        """
        response = self.client.patch('/trainings/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_all_training_returns_405(self):
        """
        A DELETE request on /trainings/ should not be possible
        """
        response = self.client.delete('/trainings/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    """
    Tests for the /trainings/<firstname>/<lastname>/ path
    """
    def test_get_training_from_employee_returns_200_when_found(self):
        """
        A GET request on /trainings/<firstname>/<lastname>/ should return an array of trainings
        """
        self.ws.append_row(["1/1/2018",1,"Testuser","Testname","Care","Text","PXL","Hasselt",1.8,"Yep","Nope"])
        response = self.client.get('/trainings/Testuser/Testname/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_training_from_employee_returns_404_when_not_found(self):
        """
        A GET request on /trainings/<firstname>/<lastname>/ should return an array of trainings
        """
        response = self.client.get('/trainings/Testuser/Testname/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_training_from_employee_returns_405(self):
        """
        A PUT request on /trainings/<firstname>/<lastname>/ should not be possible
        """
        response = self.client.post('/trainings/Testuser/Testname/?sheet=TestSheet', json.dumps(self.training_json), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_training_from_employee_returns_405(self):
        """
        A PUT request on /trainings/<firstname>/<lastname>/ should not be possible
        """
        response = self.client.put('/trainings/Testuser/Testname/?sheet=TestSheet', json.dumps(self.training_json_partial), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_training_from_employee_returns_405(self):
        """
        A PATCH request on /trainings/<firstname>/<lastname>/ should not be possible
        """
        response = self.client.patch('/trainings/Testuser/Testname/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_training_from_employee_returns_405(self):
        """
        A DELETE request on /trainings/<firstname>/<lastname>/ should not be possible
        """
        response = self.client.delete('/trainings/Testuser/Testname/?sheet=TestSheet')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)