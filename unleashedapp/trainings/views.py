from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate with Google
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Get the Training spreadsheet file
spreadsheet = client.open_by_key('1jEZR1uaEylQ05AohVvRpdQSWGOl7nDQE4oDtTWVAGkw')

@csrf_exempt
def training_list(request):
    """"
    List all training
    """
    sheet = request.GET.get('sheet', 'Data')
    worksheet = spreadsheet.worksheet(sheet)
    if request.method == 'GET':
        list_of_records = worksheet.get_all_records()
        if list_of_records == "":
            return JsonResponse([], safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse(list_of_records, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        return JsonResponse([], safe=False, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        return JsonResponse([], safe=False, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    elif request.method == 'PATCH':
        return JsonResponse([], safe=False, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    elif request.method == 'DELETE':
        return JsonResponse([], safe=False, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@csrf_exempt
def training_id(request, id):
    """"
    Get a single training
    """
    sheet = request.GET.get('sheet', 'Data')
    worksheet = spreadsheet.worksheet(sheet)
    if request.method == 'GET':
        data = []
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
            data.append(result_json)
        return JsonResponse(data, safe=False)


@csrf_exempt
def training_employee_list(request, firstname, lastname):
    """"
    List all trainings from one person
    """
    sheet = request.GET.get('sheet', 'Data')
    worksheet = spreadsheet.worksheet(sheet)
    if request.method == 'GET':
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
