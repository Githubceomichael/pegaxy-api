import pygsheets
import pandas as pd
import requests
import json
import sys
import time as time
from datetime import datetime

def convertDatetime24(epoch):
    convertedDatetime = time.strftime('%Y-%m-%d %H:%M', time.localtime(epoch))
    return convertedDatetime

def convertDatetime12(epoch):
    convertedDatetime = time.strftime('%b %d %H:%M', time.localtime(epoch))
    return convertedDatetime

now = datetime.now()
nowDatestamp = now.strftime('%m%d')
nowDatetime24 = now.strftime('%Y-%m-%d %H:%M:%S')
nowDatetime12 = now.strftime('%b %d %I:%M %p')

sys.stdout = open(nowDatestamp + ' Pegaxy Breeding Plan.txt', 'wt')

dataFinal = []
metamaskAddress = ''

masterdata = requests.get('https://api-apollo.pegaxy.io/v1/pegas/owner/user/' + str(metamaskAddress))
masterdataText = masterdata.text
masterdataParsed = json.loads(masterdataText)

pegaID = [x['id'] for x in masterdataParsed]
pegaName = [x['name'] for x in masterdataParsed]
bloodline = [x['bloodLine'] for x in masterdataParsed]
breedType = [x['breedType'] for x in masterdataParsed]
gender = [x['gender'] for x in masterdataParsed]
breedCount = [x['breedCount'] for x in masterdataParsed]
bornTime = [x['bornTime'] for x in masterdataParsed]
lastBreedTime = [x['lastBreedTime'] for x in masterdataParsed]
speed = [x['speed'] for x in masterdataParsed]
strength = [x['strength'] for x in masterdataParsed]
wind = [x['wind'] for x in masterdataParsed]
water = [x['water'] for x in masterdataParsed]
fire = [x['fire'] for x in masterdataParsed]
lightning = [x['lightning'] for x in masterdataParsed]

def breedability():
    i = 0
    x = 2
    for n in range(len(masterdataParsed)):
        totalStats = speed[i] + strength[i] + wind[i] + water[i] + fire[i] + lightning[i]
        if lastBreedTime[i] == 0:
            breedabilityTimeRaw = bornTime[i] + (86400 * 4)
            breedabilityDatetime24 = convertDatetime24(breedabilityTimeRaw)
            breedabilityDatetime12 = convertDatetime12(breedabilityTimeRaw)
            if breedabilityDatetime24 < nowDatetime24:
                breedability = 'Breedable'
            else:
                breedability = str(breedabilityDatetime12)
        else:
            if bloodline[i] == 'Hoz':
                breedabilityTimeRaw = lastBreedTime[i] + 86400
                breedabilityDatetime24 = convertDatetime24(breedabilityTimeRaw)
                breedabilityDatetime12 = convertDatetime12(breedabilityTimeRaw)
                if breedabilityDatetime24 < nowDatetime24:
                    breedability = 'Breedable'
                else:
                    breedability = str(breedabilityDatetime12)
            elif bloodline[i] == 'Campona':
                breedabilityTimeRaw = lastBreedTime[i] + (86400 * 2)
                breedabilityDatetime24 = convertDatetime24(breedabilityTimeRaw)
                breedabilityDatetime12 = convertDatetime12(breedabilityTimeRaw)
                if breedabilityDatetime24 < nowDatetime24:
                    breedability = 'Breedable'
                else:
                    breedability = str(breedabilityDatetime12)
        if breedCount[i] == 0:      
            breedCost = 2000
        elif breedCount[i] == 1:
            breedCost = 4000
        elif breedCount[i] == 2:
            breedCost = 6000
        elif breedCount[i] == 3:
            breedCost = 10000
        else:
            breedCost = 16000

        if breedCount[i] <= 1:
            print((str(pegaID[i]) + "," + str(pegaName[i]) + "," + str(bloodline[i]) + "," + str(breedType[i]) + "," + str(gender[i]) + "," + str(breedCount[i]) + "," + str(breedCost) + "," + str(breedability) + "," + str(speed[i]) + "," + str(strength[i]) + "," + str(wind[i]) + "," + str(water[i]) + "," + str(fire[i]) + "," + str(lightning[i]) + "," + str(totalStats)))
        i += 1
       

breedability()