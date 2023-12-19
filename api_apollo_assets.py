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

metamaskAddress = ''

filename = nowDatestamp + ' Assets ' + metamaskAddress + '.txt'
sys.stdout = open(filename, 'wt')



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
share = [x['lastRenterPrice'] for x in masterdataParsed]
totalRaces = [x['pegaTotalRaces'] for x in masterdataParsed]
raceability = [x['canRaceAt'] for x in masterdataParsed]
gold = [x['gold'] for x in masterdataParsed]
silver = [x['silver'] for x in masterdataParsed]
bronze = [x['bronze'] for x in masterdataParsed]
win = [x['win'] for x in masterdataParsed]
lose = [x['lose'] for x in masterdataParsed]
winRate = [x['winRate'] for x in masterdataParsed]
service = [x['service'] for x in masterdataParsed]
speed = [x['speed'] for x in masterdataParsed]
strength = [x['strength'] for x in masterdataParsed]
wind = [x['wind'] for x in masterdataParsed]
water = [x['water'] for x in masterdataParsed]
fire = [x['fire'] for x in masterdataParsed]
lightning = [x['lightning'] for x in masterdataParsed]



def masterdata():
    i = 0
    for n in range(len(masterdataParsed)):
        totalStats = speed[i] + strength[i] + wind[i] + water[i] + fire[i] + lightning[i]
        winRate100 = winRate[i] * 100
        status = convertDatetime24(raceability[i])
        if totalRaces[i] != 0:
            if service[i] == 'RENT_SERVICE':
                status = 'In Rent Service'
            elif service[i] == 'MARKET_SERVICE':
                status = 'In Market Service'
            elif service[i] == 'RACE_SERVICE':
                status = 'In Race Service'
            if breedType[i] == "Pacer":
                totalEarnings = ((gold[i]  * 42) + (silver[i] * 18) + (bronze[i] * 10)) * (share[i] * .01)
            elif breedType[i] == "Rare":
                totalEarnings = ((gold[i]  * 126) + (silver[i] * 53) + (bronze[i] * 31)) * (share[i]* .01)
            elif breedType[i] == "Epic":
                totalEarnings = ((gold[i]  * 342) + (silver[i] * 142) + (bronze[i] * 86)) * (share[i]* .01)
            elif breedType[i] == "Legendary" and breedType[i] == "Founding":
                totalEarnings = ((gold[i]  * 930) + (silver[i] * 388) + (bronze[i] * 232)) * (share[i]* .01)
            if totalRaces[i] > 200:
                accuracy = "Accurate"
            else:
                accuracy = "Inaccurate"
            print(str(pegaID[i]) + "," + str(pegaName[i]) + "," + str(breedType[i]) + "," + str(bloodline[i]) + "," + str(gender[i]) + "," + str(breedCount[i]) + "," + str(sharePercentage[i]) + "," + str(renter[i]) + "," + str(status) + "," + str(speed[i]) + "," + str(strength[i]) + "," + str(wind[i]) + "," + str(water[i]) + "," + str(fire[i]) + "," + str(lightning[i]) + "," + str(totalStats) + "," + str(gold[i]) + "," + str(silver[i]) + "," + str(bronze[i]) + "," + str(totalRaces[i]) + "," + str(winRate100) + "," +  str(accuracy)+ "," + str(totalEarnings))
        else:
            print(str(pegaID[i]) + "," + str(pegaName[i]) + "," + str(breedType[i]) + "," + str(bloodline[i]) + "," + str(gender[i]) + "," + str(breedCount[i]) + "," + str(sharePercentage[i]) + "," + str(renter[i]) + "," + str(status)+ "," + str(speed[i]) + "," + str(strength[i]) + "," + str(wind[i]) + "," + str(water[i]) + "," + str(fire[i]) + "," + str(lightning[i]) + "," + str(totalStats))
        i += 1

masterdata()