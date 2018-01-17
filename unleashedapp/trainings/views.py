from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
import gspread
import logging
import json
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate with Google
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

logger = logging.getLogger(__name__)

# Get the Training spreadsheet file
spreadsheet = client.open_by_key('1jEZR1uaEylQ05AohVvRpdQSWGOl7nDQE4oDtTWVAGkw')


class TrainingList(APIView):
    def get(self, request, format=None):
        sheet = request.GET.get('sheet', 'Data')
        worksheet = spreadsheet.worksheet(sheet)
        list_of_records = worksheet.get_all_records()
        if list_of_records == "":
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse(list_of_records, safe=False, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        sheet = request.GET.get('sheet', 'Data')
        worksheet = spreadsheet.worksheet(sheet)
        data = json.loads(request.body.decode('utf-8'))
        if "date" in data and "days" in data and "firstname" in data and "lastname" in data and "team" in data and "training" in data and "company" in data and "city" in data and "cost" in data and "invoice" in data and "info" in data:
            worksheet.append_row([data["date"], data["days"], data["firstname"], data["lastname"], data["team"], data["training"], data["company"], data["city"], data["cost"], data["invoice"], data["info"]])
            return JsonResponse(data, safe=False, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse("[]", safe=False, status=status.HTTP_400_BAD_REQUEST)


class TrainingDetail(APIView):
    def get(self, request, id, format=None):
        """
        GET a single training
        """
        sheet = request.GET.get('sheet', 'Data')
        worksheet = spreadsheet.worksheet(sheet)
        result = []
        row_value = worksheet.range(id, 1, id, 11)
        if row_value[0].value != "":
            result_json = {
                "date": row_value[0].value,
                "days": row_value[1].value,
                "firstname": row_value[2].value,
                "lastname": row_value[3].value,
                "team": row_value[4].value,
                "training": row_value[5].value,
                "company": row_value[6].value,
                "city": row_value[7].value,
                "cost": row_value[8].value,
                "invoice": row_value[9].value,
                "info": row_value[10].value,
            }
            result.append(result_json)
            return JsonResponse(result, safe=False)
        else:
            return JsonResponse("[]", safe=False, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        """
        PUT a row into the spreadsheet
        """
        if id == "1":
            # In this context, id 1 is the row of headings, this shouldn't be overwritten
            return JsonResponse("[]", safe=False, status=status.HTTP_404_NOT_FOUND)
        else:
            sheet = request.GET.get('sheet', 'Data')
            worksheet = spreadsheet.worksheet(sheet)
            data = json.loads(request.body.decode('utf-8'))
            # Get the data from the current row
            result = []
            row_value = worksheet.range(id, 1, id, 11)
            if row_value[0].value != "":
                if "date" in data or "days" in data or "firstname" in data or "lastname" in data or "team" in data or "training" in data or "company" in data or "city" in data or "cost" in data or "invoice" in data or "info" in data:
                    if "date" in data:
                        worksheet.update_cell(id, 1, data['date'])
                    if "days" in data:
                        worksheet.update_cell(id, 2, data['days'])
                    if "firstname" in data:
                        worksheet.update_cell(id, 3, data['firstname'])
                    if "lastname" in data:
                        worksheet.update_cell(id, 4, data['lastname'])
                    if "team" in data:
                        worksheet.update_cell(id, 5, data['team'])
                    if "training" in data:
                        worksheet.update_cell(id, 6, data['training'])
                    if "company" in data:
                        worksheet.update_cell(id, 7, data['company'])
                    if "city" in data:
                        worksheet.update_cell(id, 8, data['city'])
                    if "cost" in data:
                        worksheet.update_cell(id, 9, data['cost'])
                    if "invoice" in data:
                        worksheet.update_cell(id, 10, data['invoice'])
                    if "info" in data:
                        worksheet.update_cell(id, 11, data['info'])
                    return JsonResponse("[]", safe=False, status=status.HTTP_201_CREATED)
                else:
                    return JsonResponse("[]", safe=False, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse("[]", safe=False, status=status.HTTP_404_NOT_FOUND)


class TrainingAllDetail(APIView):
    def get(self, request, firstname, lastname, format=None):
        """
        List all trainings from one person
        """
        sheet = request.GET.get('sheet', 'Data')
        worksheet = spreadsheet.worksheet(sheet)
        cell_list = worksheet.findall(firstname)
        data = []
        for cell in cell_list:
            row_value = worksheet.range(cell.row, 1, cell.row, 11)
            if row_value[2].value == firstname and row_value[3].value == lastname:
                result_json = {
                    "date": row_value[0].value,
                    "days": row_value[1].value,
                    "firstname": row_value[2].value,
                    "lastname": row_value[3].value,
                    "team": row_value[4].value,
                    "training": row_value[5].value,
                    "company": row_value[6].value,
                    "city": row_value[7].value,
                    "cost": row_value[8].value,
                    "invoice": row_value[9].value,
                    "info": row_value[10].value,
                }
                data.append(result_json)
        return JsonResponse(data, safe=False)
