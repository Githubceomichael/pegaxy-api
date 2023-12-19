from winreg import REG_REFRESH_HIVE
import requests
import json
import webbrowser

i = 
error = 0

rentAPI = requests.get('https://api.pegaxy.io/rent/listing/' + str(i))
rentUrl = 'https://play.pegaxy.io/renting/listing/' + str(i)
status = rentAPI.status_code

while status != 404:
    rentData = rentAPI.text
    rentDataParsed = json.loads(rentData)

    rentMode = rentDataParsed['listing']['rentMode']
    share = int(rentDataParsed['listing']['price'])
    desiredShare = 10000

    if status != 404 and share > desiredShare:
        webbrowser.open(rentUrl, new=1)
        i += 1