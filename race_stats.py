import pygsheets
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

filename = nowDatestamp + '_apollo.txt'
sys.stdout = open(filename, 'wt')

metamaskAddress = ''

masterdata = requests.get('https://api-apollo.pegaxy.io/v1/pegas/owner/user/' + str(metamaskAddress))
masterdataText = masterdata.text
masterdataParsed = json.loads(masterdataText)

pegaID = [x['id'] for x in masterdataParsed]
pegaName = [x['name'] for x in masterdataParsed]
renter = [x['renterAddress'] for x in masterdataParsed]
sharePercentage = [x['lastRenterPrice'] for x in masterdataParsed]
energy = [x['energy'] for x in masterdataParsed]
lastRace = [x['lastReduceEnergy'] for x in masterdataParsed]
service = [x['service'] for x in masterdataParsed]
gender = [x['gender'] for x in masterdataParsed]
bloodline = [x['bloodLine'] for x in masterdataParsed]
breedType = [x['breedType'] for x in masterdataParsed]
breedCount = [x['breedCount'] for x in masterdataParsed]
bornTime = [x['bornTime'] for x in masterdataParsed]
lastBreedTime = [x['lastBreedTime'] for x in masterdataParsed]
totalRaces = [x['pegaTotalRaces'] for x in masterdataParsed]
raceability = [x['canRaceAt'] for x in masterdataParsed]
gold = [x['gold'] for x in masterdataParsed]
silver = [x['silver'] for x in masterdataParsed]
bronze = [x['bronze'] for x in masterdataParsed]
winRate = [x['winRate'] for x in masterdataParsed]
service = [x['service'] for x in masterdataParsed]



def masterdata():
    i = 0
    for n in range(len(masterdataParsed)):
        winRate100 = winRate[i] * 100
        status = convertDatetime24(raceability[i])
        if totalRaces[i] != 0:
            if service[i] == 'RENT_SERVICE':
                status = 'In Rent Service'
            elif service[i] == 'MARKET_SERVICE':
                status = 'In Market Service'
            elif service[i] == 'RACE_SERVICE':
                status = 'In Race Service'
            if totalRaces[i] > 200:
                accuracy = "Accurate"
            else:
                accuracy = "Inaccurate"
            totalEarnings = ((gold[i]  * 105) + (silver[i] * 44) + (bronze[i] * 26))/ totalRaces[i]
            winrateGS = (gold[i] + silver[i])/totalRaces[i] 
            print(str(pegaID[i]) + "," + str(pegaName[i]) + "," + str(energy[i]) + "," + str(bloodline[i]) + "," + str(gender[i]) + "," + str(breedCount[i]) + "," + str(sharePercentage[i]) + "," + str(renter[i]) + "," + str(status) + "," + str(gold[i]) + "," + str(silver[i]) + "," + str(bronze[i]) + "," + str(winrateGS) + "," + str(winRate100) + "," +  str(accuracy)+ "," + str(totalEarnings))
        else:
            print(str(pegaID[i]) + "," + str(pegaName[i]) + "," + str(energy[i]) + "," + str(bloodline[i]) + "," + str(gender[i]) + "," + str(breedCount[i]) + "," + str(sharePercentage[i]) + "," + str(renter[i]) + "," + str(status))
        i += 1

masterdata()