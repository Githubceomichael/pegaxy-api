import requests
import json
import sys
import time as time
from datetime import datetime
from tabulate import tabulate

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

#sys.stdout = open(nowDatestamp + '_assets.txt', 'wt')

masterdata = []
masterdataHeader = ['Pega ID', 'Pega Name', 'Bloodline', 'Type', 'Gender', 'Count', 'Status','Energy', 'Last Race', 'Status', 'Gold', 'Silver', 'Bronze', 'Winrate', 'Overall Winrate', 'Owner', 'Renter',  'Total']

ownerEarningsData =[]
renterEarningsData = []



ownedPega = []

i = 0

for n in range(len(ownedPega)):

    # Breeding Data
    breedingAPI = requests.get('https://api.pegaxy.io/pega/' + str(ownedPega[i]))
    breedingMasterdataRaw = breedingAPI.text
    print(breedingMasterdataRaw)
    breedingMasterdataParsed = json.loads(breedingMasterdataRaw)

    pegaID = breedingMasterdataParsed['pega']['id']
    name = breedingMasterdataParsed['pega']['name']
    bloodline = breedingMasterdataParsed['pega']['bloodLine']
    breedType = breedingMasterdataParsed['pega']['breedType']
    gender = breedingMasterdataParsed['pega']['gender']
    breedCount = breedingMasterdataParsed['pega']['breedTime']
    lastBreedTime = breedingMasterdataParsed['pega']['lastBreedTime']
    bornTime = breedingMasterdataParsed['pega']['bornTime']

    if lastBreedTime == 0:
        breedabilityTimeRaw = bornTime + (86400 * 4)
        breedabilityDatetime24 = convertDatetime24(breedabilityTimeRaw)
        breedabilityDatetime12 = convertDatetime12(breedabilityTimeRaw)
        if breedabilityDatetime24 < nowDatetime24:
            breedability = 'Breedable'
        else:
            breedability = 'Breedable in ' + str(breedabilityDatetime12)
    else:
        if bloodline == 'Hoz':
            breedabilityTimeRaw = lastBreedTime + 86400
            breedabilityDatetime24 = convertDatetime24(breedabilityTimeRaw)
            breedabilityDatetime12 = convertDatetime12(breedabilityTimeRaw)
            if breedabilityDatetime24 < nowDatetime24:
                breedability = 'Breedable'
            else:
                breedability = 'Breedable in ' + str(breedabilityDatetime12)
        elif bloodline == 'Campona':
            breedabilityTimeRaw = lastBreedTime + (86400 * 2)
            breedabilityDatetime24 = convertDatetime24(breedabilityTimeRaw)
            breedabilityDatetime12 = convertDatetime12(breedabilityTimeRaw)
            if breedabilityDatetime24 < nowDatetime24:
                breedability = 'Breedable'
            else:
                breedability = 'Breedable in ' + str(breedabilityDatetime12)


    #Racing Data
    racingAPI = requests.get('https://api.pegaxy.io/race/history/pega/' + str(ownedPega[i]))
    racingMasterdataRaw = racingAPI.text
    racingMasterdataParsed = json.loads(racingMasterdataRaw)

    energyRaw = breedingMasterdataParsed['pega']['energy']
    lastRaceTimeRaw = breedingMasterdataParsed['pega']['lastReduceEnergy']
    lastRaceTime = convertDatetime12(lastRaceTimeRaw)
    raceStatus = breedingMasterdataParsed['pega']['inRace']
    serviceRaw = breedingMasterdataParsed['pega']['inService']
    raceability = breedingMasterdataParsed['pega']['canRace']
    if raceability == True:
        energy = energyRaw
        if raceStatus == '':
            if serviceRaw == 'RENT_SERVICE':
                service = 'In Rent Service'
            elif serviceRaw == 'MARKET_SERVICE':
                service = 'In Market Service'
            elif serviceRaw == 'RACE_SERVICE':
                service = 'In Race Service'
            else:
                service = 'No Service'
            status = service
        else:
            status = 'In Race'
    else:
        energy = 0
        if bloodline == 'Hoz':
            raceabilityTimeRaw = bornTime + (86400)
            raceabilityDatetime12 = convertDatetime12(raceabilityTimeRaw)
            status = 'Raceable in ' + str(raceabilityDatetime12)
        elif bloodline == 'Campona':
            raceabilityTimeRaw = bornTime + (86400 * 2)
            raceabilityDatetime12 = convertDatetime12(raceabilityTimeRaw)
            status = 'Raceable in ' + str(raceabilityDatetime12)

    racingDataRaw = racingMasterdataParsed['data']
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
        renterEarnings = earnings * 0.05
        renterEarningsData.append(renterEarnings)
        ownerEarnings = earnings - renterEarnings
        ownerEarningsData.append(ownerEarnings)
        
    else:
        earnings = sum(rewards)
        winrate = 0
        renterEarnings = 0
        renterEarningsData.append(renterEarnings)
        ownerEarnings = 0
        ownerEarningsData.append(ownerEarnings)

    win = breedingMasterdataParsed['pega']['win']
    lose = breedingMasterdataParsed['pega']['lose']

    if lose != 0:
        overallWinrate = (win / (win + lose)) * 100
    else:
        overallWinrate = 0

    dataRaw = []
    dataRaw.append(str(pegaID) + ",")
    dataRaw.append(str(name) + ",")
    dataRaw.append(str(bloodline) + ",")
    dataRaw.append(str(breedType) + ",")
    dataRaw.append(str(gender) + ",")
    dataRaw.append(str(breedCount) + ",")
    dataRaw.append(str(breedability) + ",")
    dataRaw.append(str(energy) + ",")
    dataRaw.append(str(lastRaceTime) + ",")
    dataRaw.append(str(status) + ",")
    dataRaw.append(str(gold) + ",")
    dataRaw.append(str(silver) + ",")
    dataRaw.append(str(bronze) + ",")
    dataRaw.append(str(winrate) + ",")
    dataRaw.append(str(overallWinrate) + ",")
    dataRaw.append(str(ownerEarnings) + ",")
    dataRaw.append(str(renterEarnings) + ",")
    dataRaw.append(str(earnings) + ",")
    masterdata.append(dataRaw)

    i += 1


print(' |', nowDatetime12)
print('')
print('-------------------------------------------------------------------------Breeding Data-------------------------------------------------------------------------')
print(tabulate(masterdata, headers = masterdataHeader))
print('')

print('Racing Data Summary for the Last 100 Races per Pega')
print("Total Owned Pegas: " + str(len(ownedPega)))
print("Total Owner Earnings: " + str(sum(ownerEarningsData)))
print("Total Renter Earnings: " + str(sum(renterEarningsData)))
print('')