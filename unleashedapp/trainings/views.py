from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate with Google
scope = ['https://spreadsheets.google.com/feeds']
## TODO: This can't be an absolute path, won't work for anybody else with a different path
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Python/backend/unleashedapp/trainings/client_secret.json', scope)
client = gspread.authorize(creds)

# Get the Training spreadsheet file
sheet = client.open_by_key('1jEZR1uaEylQ05AohVvRpdQSWGOl7nDQE4oDtTWVAGkw').sheet1

@csrf_exempt
def training_list(request):
    """"
    List all training
    """
    if request.method == 'GET':
        list_of_hashes = sheet.get_all_records()
        return JsonResponse(list_of_hashes, safe=False)

@csrf_exempt
def training_employee_list(request, firstname, lastname):
    """"
    List all training
    """
    if request.method == 'GET':
        cell_list = sheet.findall(firstname)
        data = []
        for cell in cell_list:
            row_value = sheet.range(cell.row, 1, cell.row, 11)
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
