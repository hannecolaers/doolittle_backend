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
def training_employee_list(request, lookup):
    """"
    List all training
    """
    if request.method == 'GET':
        cell_list = sheet.find(lookup)
        #for cell in cell_list
        row_value = sheet.range(cell_list.row, 1, cell_list.row, 11)
        result_json = [ {
            "Date of the event": row_value[0].value,
            "Days": row_value[1].value,
            "Name": row_value[2].value,
            "Last Name": row_value[3].value,
            "Team": row_value[4].value,
            "Training / Event / Hotel": row_value[5].value,
            "Company": row_value[6].value,
            "City": row_value[7].value,
            "Cost / Euro": row_value[8].value,
            "Invoice to finance?": row_value[9].value,
            "Extra info": row_value[10].value,
        } ]
        return JsonResponse(result_json, safe=False)