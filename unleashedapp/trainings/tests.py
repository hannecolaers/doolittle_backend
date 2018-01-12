from django.urls import reverse
from django.test import TestCase, Client, RequestFactory
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SquadTestCase(TestCase):
    def setUp(self):
        # Authenticate with Google
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        # Create a new, empty spreadsheet and worksheet
        self.sh = client.create('SpreadTest')
        self.sh.share('pxl.unleashed@gmail.com', perm_type='user', role='writer')
        self.ws = self.sh.add_worksheet(title="TextSheet", rows="100", cols="12")
        # Add the heading rows
        self.ws.insert_row(["date", "days", "firstname", "lastname", "team", "training", "company", "city", "cost", "invoice", "info"])
        self.training_json = [
            {
                "date": "1/1/2018",
                "days": 1,
                "firstname": "Yannick",
                "lastname": "Franssen",
                "team": "Unleashed",
                "training": "Django",
                "company": "PXL",
                "city": "Hasselt",
                "cost": 1.8,
                "invoice": "Yep",
                "info": "Nope"
            }
        ]

    """
    Tests for the /trainings/ path
    """
    def test_get_all_training_returns_200_when_found(self):
        """
        A GET request on /trainings/ should return an array of trainings
        """
        response = self.client.get('/trainings/')
        self.ws.insert_row(["1/1/2018",1,"Yannick","Franssen","Unleashed","Django","PXL","Hasselt",1.8,"Yep","Nope"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, self.training_json)

    def test_get_all_training_returns_200_when_non_found(self):
        """
        A GET request on /trainings/ should still work with no results and return an empty array
        """
        response = self.client.get('/trainings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)