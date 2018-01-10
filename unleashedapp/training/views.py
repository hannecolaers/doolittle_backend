from django.shortcuts import render
import gspread

# Authenticate with Google
gc = gspread.login('pxl.unleashed@gmail.com', 'unlea5hed')

# Get the Training spreadsheet file
sh = gc.open_by_key('1jEZR1uaEylQ05AohVvRpdQSWGOl7nDQE4oDtTWVAGkw')
worksheet = sh.get_worksheet(0)

