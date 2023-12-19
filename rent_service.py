import pandas as pd
import requests
import json
import sys
import time as time
from datetime import datetime

def convertDatetime24(epoch):
    convertedDatetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
    return convertedDatetime

def convertDatetime12(epoch):
    convertedDatetime = time.strftime('%b %d %I:%M %p', time.localtime(epoch))
    return convertedDatetime

now = datetime.now()    
nowDatestamp = now.strftime('%m%d')
nowDatetime24 = now.strftime('%Y-%m-%d %H:%M:%S')
nowDatetime12 = now.strftime('%b %d %I:%M %p')

sys.stdout = open(nowDatestamp + '_rents.txt', 'wt')

metamaskAddress = ''

masterdata = requests.get('https://api-apollo.pegaxy.io/v1/pegas/owner/user/' + str(metamaskAddress))
masterdataText = masterdata.text
masterdataParsed = json.loads(masterdataText)

pegaID = [x['id'] for x in masterdataParsed]
pegaName = [x['name'] for x in masterdataParsed]

def rents():
    i = 0
    for n in range(len(masterdataParsed)):
        rentingData = requests.get('https://api-apollo.pegaxy.io/v1/game-api/rent/history/' + str(pegaID[i]))
        rentingDataText = rentingData.text
        rentingDataParsed = json.loads(rentingDataText)
        rentingDataRaw = rentingDataParsed['history']
        rentDateRaw = [x['rentAt'] for x in rentingDataRaw]
        renterRaw = [x['renter']['address'] for x in rentingDataRaw]
        if len(rentingDataRaw) != 0:
            rentDate = str(convertDatetime24(rentDateRaw[0]))
            renter = renterRaw[0]
        else: 
            rentDate = 0
            renter = 0
        print(str(pegaID[i]) + "," + str(pegaName[i]) + "," + str(rentDate) + "," + str(renter))
        i += 1

rents()