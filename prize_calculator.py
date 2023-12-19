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

sys.stdout = open(nowDatestamp + '_races.txt', 'wt')

dataFinal = []
metamaskAddress = ''

masterdata = requests.get('https://api-apollo.pegaxy.io/v1/pegas/owner/user/' + str(metamaskAddress))
masterdataText = masterdata.text
masterdataParsed = json.loads(masterdataText)

pegaID = [x['id'] for x in masterdataParsed]
pegaName = [x['name'] for x in masterdataParsed]
i = 0

def races():
    global i
    for n in range(len(pegaID)):
        racingData = requests.get('https://api-apollo.pegaxy.io/v1/game-api/race/history/pega/' + str(pegaID[i]))
        racingDataText = racingData.text
        racingDataParsed = json.loads(racingDataText)

        racingDataRaw = racingDataParsed['data']
        raceNumber = 99
        positions = []
        rewards =[]
        gold = 0
        silver = 0
        bronze = 0
        wins = 0
        for data in racingDataRaw:
            for key, value in data.items():
                if key == 'position':
                    if value == 1:
                        gold += 1
                        wins += 1
                    elif value == 2:
                        silver += 1
                        wins += 1
                    elif value == 3:
                        bronze += 1
                        wins += 1
                    positions.append(str(value))
                if key == 'reward':
                    rewards.append(value)
                raceNumber -= 1

        if len(positions) != 0:
            winrateRaw = ((gold + silver + bronze) / len(positions)) * 100
            winrate = round(winrateRaw, 2)
            earnings = sum(rewards)

        else:
            earnings = sum(rewards)
            winrate = 0
            
        print(str(pegaID[i]) + "," + str(pegaName[i]) + "," + str(earnings))
        i+=1

races()