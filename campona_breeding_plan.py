import pygsheets
import pandas as pd
import requests
import json
import sys
import time as time
from datetime import datetime

gc = pygsheets.authorize(service_file='')
sh = gc.open('Pegaxy Breeding Plan')
df = pd.DataFrame()
wks = sh[0]


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

sys.stdout = open(nowDatestamp + '_campona.txt', 'wt')

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

def breedability():
    i = 0
    x = 2
    for n in range(len(masterdataParsed)):
        if lastBreedTime[i] == 0:
            breedabilityTimeRaw = bornTime[i] + (86400 * 4)
            breedabilityDatetime24 = convertDatetime24(breedabilityTimeRaw)
            breedabilityDatetime12 = convertDatetime12(breedabilityTimeRaw)
            if breedabilityDatetime24 < nowDatetime24:
                breedability = 'Breedable'
            else:
                breedability = 'Breedable in ' + str(breedabilityDatetime12)
        else:
            if bloodline[i] == 'Hoz':
                breedabilityTimeRaw = lastBreedTime[i] + 86400
                breedabilityDatetime24 = convertDatetime24(breedabilityTimeRaw)
                breedabilityDatetime12 = convertDatetime12(breedabilityTimeRaw)
                if breedabilityDatetime24 < nowDatetime24:
                    breedability = 'Breedable'
                else:
                    breedability = 'Breedable in ' + str(breedabilityDatetime12)
            elif bloodline[i] == 'Campona':
                breedabilityTimeRaw = lastBreedTime[i] + (86400 * 2)
                breedabilityDatetime24 = convertDatetime24(breedabilityTimeRaw)
                breedabilityDatetime12 = convertDatetime12(breedabilityTimeRaw)
                if breedabilityDatetime24 < nowDatetime24:
                    breedability = 'Breedable'
                else:
                    breedability = 'Breedable in ' + str(breedabilityDatetime12)
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

        if breedCount[i] == 0 and bloodline[i] == 'Campona':
            #wks.update_value('A'+str(x), (str(pegaID[i]) + "," + str(pegaName[i]) + "," + str(bloodline[i]) + "," + str(breedType[i]) + "," + str(gender[i]) + "," + str(breedCount[i]) + "," + str(breedCost) + "," + str(breedability)))
            #x += 1
            print((str(pegaID[i]) + "," + str(pegaName[i]) + "," + str(bloodline[i]) + "," + str(breedType[i]) + "," + str(gender[i]) + "," + str(breedCount[i]) + "," + str(breedCost) + "," + str(breedability)))
        i += 1
       

breedability()