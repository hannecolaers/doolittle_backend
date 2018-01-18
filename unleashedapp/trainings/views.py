from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
import gspread
import json
import logging
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate with Google
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Get the Training spreadsheet file
spreadsheet = client.open_by_key('1jEZR1uaEylQ05AohVvRpdQSWGOl7nDQE4oDtTWVAGkw')

logger = logging.getLogger(__name__)

def generate_json(row):
    return {
        "date": row[0].value,
        "days": row[1].value,
        "firstname": row[2].value,
        "lastname": row[3].value,
        "team": row[4].value,
        "training": row[5].value,
        "company": row[6].value,
        "city": row[7].value,
        "cost": row[8].value,
        "invoice": row[9].value,
        "info": row[10].value
    }

def get_sheet(sheet):
    return spreadsheet.worksheet(sheet)

def validate_data_has_all(data):
    return True if "date" in data and "days" in data and "firstname" in data and "lastname" in data and "team" in data and "training" in data and "company" in data and "city" in data and "cost" in data and "invoice" in data and "info" in data else False

def validate_data_has_one(data):
    return True if "date" in data or "days" in data or "firstname" in data or "lastname" in data or "team" in data or "training" in data or "company" in data or "city" in data or "cost" in data or "invoice" in data or "info" in data else False


class TrainingList(APIView):
    def get(self, request):
        worksheet = get_sheet(request.GET.get('sheet', 'Data'))
        list_of_records = worksheet.get_all_records()
        return JsonResponse(list_of_records, safe=False, status=status.HTTP_200_OK)

    def post(self, request):
        worksheet = get_sheet(request.GET.get('sheet', 'Data'))
        data = json.loads(request.body.decode('utf-8'))
        if validate_data_has_all(data):
            worksheet.append_row([data["date"], data["days"], data["firstname"], data["lastname"], data["team"], data["training"], data["company"], data["city"], data["cost"], data["invoice"], data["info"]])
            return JsonResponse(data, safe=False, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse([], safe=False, status=status.HTTP_400_BAD_REQUEST)


class TrainingDetail(APIView):
    def get(self, request, id):
        """
        GET a single training
        """
        worksheet = get_sheet(request.GET.get('sheet', 'Data'))
        if int(id) == 1: # 1 is the row of headings
            return JsonResponse([], safe=False, status=status.HTTP_400_BAD_REQUEST)
        elif worksheet.row_count < int(id):
            return JsonResponse([], safe=False, status=status.HTTP_404_NOT_FOUND)
        else:
            row_value = worksheet.range(int(id), 1, int(id), 11)
            if row_value[0].value == "":
                return JsonResponse([], safe=False, status=status.HTTP_404_NOT_FOUND)
            else:
                result = []
                result.append(generate_json(row_value))
                return JsonResponse(result, safe=False)

    def put(self, request, id):
        """
        PUT a row into the spreadsheet
        """
        worksheet = get_sheet(request.GET.get('sheet', 'Data'))
        if int(id) == 1: # 1 is the row of headings
            return JsonResponse([], safe=False, status=status.HTTP_400_BAD_REQUEST)
        elif worksheet.row_count < int(id):
            return JsonResponse([], safe=False, status=status.HTTP_404_NOT_FOUND)
        else:
            data = json.loads(request.body.decode('utf-8'))
            # Get the data from the current row
            row_value = worksheet.range(int(id), 1, int(id), 11)
            if row_value[0].value == "":
                return JsonResponse([], safe=False, status=status.HTTP_404_NOT_FOUND)
            else:
                result = []
                if validate_data_has_one(data):
                    if "date" in data:
                        worksheet.update_cell(int(id), 1, data['date'])
                    if "days" in data:
                        worksheet.update_cell(int(id), 2, data['days'])
                    if "firstname" in data:
                        worksheet.update_cell(int(id), 3, data['firstname'])
                    if "lastname" in data:
                        worksheet.update_cell(int(id), 4, data['lastname'])
                    if "team" in data:
                        worksheet.update_cell(int(id), 5, data['team'])
                    if "training" in data:
                        worksheet.update_cell(int(id), 6, data['training'])
                    if "company" in data:
                        worksheet.update_cell(int(id), 7, data['company'])
                    if "city" in data:
                        worksheet.update_cell(int(id), 8, data['city'])
                    if "cost" in data:
                        worksheet.update_cell(int(id), 9, data['cost'])
                    if "invoice" in data:
                        worksheet.update_cell(int(id), 10, data['invoice'])
                    if "info" in data:
                        worksheet.update_cell(int(id), 11, data['info'])
                    # Request the updated row
                    row_value = worksheet.range(int(id), 1, int(id), 11)
                    result.append(generate_json(row_value))
                    return JsonResponse(result, safe=False, status=status.HTTP_200_OK)
                else:
                    return JsonResponse([], safe=False, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """
        DELETE a row from the spreadsheet
        """
        worksheet = get_sheet(request.GET.get('sheet', 'Data'))
        if int(id) == 1: # 1 is the row of headings
            return JsonResponse([], safe=False, status=status.HTTP_400_BAD_REQUEST)
        elif worksheet.row_count < int(id):
            return JsonResponse([], safe=False, status=status.HTTP_404_NOT_FOUND)
        else:
            worksheet.delete_row(int(id))
            return JsonResponse([], safe=False, status=status.HTTP_204_NO_CONTENT)


class TrainingAllDetail(APIView):
    def get(self, request, firstname, lastname):
        """
        List all trainings from one person
        """
        worksheet = get_sheet(request.GET.get('sheet', 'Data'))
        cell_list = worksheet.findall(firstname)
        data = []
        for cell in cell_list:
            row_value = worksheet.range(cell.row, 1, cell.row, 11)
            if row_value[2].value == firstname and row_value[3].value == lastname:
                result_json = generate_json(row_value)
                data.append(result_json)
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
