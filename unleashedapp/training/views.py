from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate with Google
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Get the Training spreadsheet file
sheet = client.open_by_key('1jEZR1uaEylQ05AohVvRpdQSWGOl7nDQE4oDtTWVAGkw').sheet1

list_of_hashes = sheet.get_all_records()