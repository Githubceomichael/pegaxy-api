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

sys.stdout = open(nowDatestamp + '_assets.txt', 'wt')

masterdata = []
masterdataHeader = ['Pega ID', 'Pega Name', 'Bloodline', 'Type', 'Gender', 'Owner']

ownerEarningsData =[]
renterEarningsData = []

ownedPega =[]

i = 0

for n in range(len(ownedPega)):

    # Breeding Data
    breedingAPI = requests.get('https://api-apollo.pegaxy.io/v1/game-api/pega/' + str(ownedPega[i]))
    breedingMasterdataRaw = breedingAPI.text
    breedingMasterdataParsed = json.loads(breedingMasterdataRaw)

    pegaID = breedingMasterdataParsed['pega']['id']
    name = breedingMasterdataParsed['pega']['name']
    bloodline = breedingMasterdataParsed['pega']['bloodLine']
    breedType = breedingMasterdataParsed['pega']['breedType']
    gender = breedingMasterdataParsed['pega']['gender']
    owner = breedingMasterdataParsed['pega']['owner']['address']

    dataRaw = []
    dataRaw.append(str(pegaID) + ",")
    dataRaw.append(str(name) + ",")
    dataRaw.append(str(bloodline) + ",")
    dataRaw.append(str(breedType) + ",")
    dataRaw.append(str(gender) + ",")
    dataRaw.append(str(owner) + ",")
    masterdata.append(dataRaw)

    i += 1

print('-------------------------------------------------------------------------Breeding Data-------------------------------------------------------------------------')
print(tabulate(masterdata, headers = masterdataHeader))
print('')