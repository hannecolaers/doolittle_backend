from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate with Google
scope = ['https://spreadsheets.google.com/feeds']
## TODO: This can't be an absolute path, won't work for anybody else with a different path
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Python/backend/unleashedapp/training/client_secret.json', scope)
client = gspread.authorize(creds)

# Get the Training spreadsheet file
sheet = client.open_by_key('1jEZR1uaEylQ05AohVvRpdQSWGOl7nDQE4oDtTWVAGkw').sheet1

list_of_hashes = sheet.get_all_records()
print(list_of_hashes)