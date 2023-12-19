#import pygsheets
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

filename = nowDatestamp + ' Pacer Share Checker ' + metamaskAddress + '.txt'
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
direct = [x['lastRenterIsDirect'] for x in masterdataParsed]
service = [x['service'] for x in masterdataParsed]
gender = [x['gender'] for x in masterdataParsed]
bloodline = [x['bloodLine'] for x in masterdataParsed]
breedType = [x['breedType'] for x in masterdataParsed]
breedCount = [x['breedCount'] for x in masterdataParsed]
bornTime = [x['bornTime'] for x in masterdataParsed]
lastBreedTime = [x['lastBreedTime'] for x in masterdataParsed]
share = [x['lastRenterPrice'] for x in masterdataParsed]
totalRaces = [x['totalRaces'] for x in masterdataParsed]
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
        lastRaceTime = convertDatetime24(lastRace[i])
        if totalRaces[i] != 0 and breedType[i] == "Pacer":
            if service[i] == 'RENT_SERVICE' and direct[i] == True:
                status = 'Direct'
            if service[i] == 'RENT_SERVICE' and direct[i] == False:
                status = 'Public'
            elif service[i] == 'MARKET_SERVICE':
                status = 'In Market Service'
            elif service[i] == 'RACE_SERVICE':
                status = 'In Race Service'
            scholarEarnings = ((((gold[i]  * 42) + (silver[i] * 18) + (bronze[i] * 10)) / totalRaces[i])) * (share[i]* .01)
            totalEarnings = ((gold[i]  * 42) + (silver[i] * 18) + (bronze[i] * 10)) / totalRaces[i]
            preferredSharePublic = (1/totalEarnings)*100
            preferredShare = (4/totalEarnings)*100
            goldEarnings = gold[i] * 42
            silverEarnings = silver[i] * 18
            bronzeEarnings = bronze[i] * 10
            if totalRaces[i] > 200:
                accuracy = "Accurate"
            else:
                accuracy = "Inaccurate"
            print(str(energy[i]) + "," + "https://play.pegaxy.io/my-assets/pega/"+str(pegaID[i]) + "," + str(pegaName[i]) + "," + str(breedType[i]) + "," + str(bloodline[i]) + "," + str(gender[i]) + "," + str(breedCount[i]) + "," + str(renter[i]) + "," + str(status) + "," + str(totalRaces[i]) + ","  + str(gold[i])  + "," + str(silver[i]) + "," + str(bronze[i])  + ","  + str(goldEarnings) + "," + str(silverEarnings) + "," + str(bronzeEarnings) + "," + str(scholarEarnings) + "," + str(totalEarnings) + "," + str(winRate100)+ "," + str(lastRaceTime)+ "," + str(sharePercentage[i])+ "," + str(preferredShare)+ "," + str(preferredSharePublic))
        elif totalRaces[i] == 0 and breedType[i] == "Pacer":
            print(str(energy[i]) + "," + "https://play.pegaxy.io/my-assets/pega/"+ str(pegaID[i]) + "," + str(pegaName[i]) + "," + str(breedType[i]) + "," + str(bloodline[i]) + "," + str(gender[i]) + "," + str(breedCount[i]) + "," + str(renter[i]) + "," + str(status))
        i += 1

masterdata()