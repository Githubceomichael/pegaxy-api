import requests
import json
import sys
from datetime import date
from datetime import datetime
from tabulate import tabulate

desiredBloodline = 'Hoz'
desiredBreedType = 'Pacer'

date = date.today()
datestamp = date.strftime("%y%m%d")

time = datetime.now()
timestamp = time.strftime("%H:%M:%S")

sys.stdout = open(datestamp + '_' + desiredBloodline + '.txt', 'wt')

masterdataInactiveListings = []
masterdataInactiveListingsHeader = ['Listing ID', 'Pega ID', 'Bloodline', 'Type', 'Count', 'Gender', 'Price']

masterdataInactiveListings = []
masterdataInactiveListingsHeader = ['Listing ID', 'Pega ID', 'Bloodline', 'Type', 'Count', 'Gender', 'Price']
        
breedCount0PricelistInactiveListings = []
breedCount1PricelistInactiveListings = []
breedCount2PricelistInactiveListings = []
breedCount3PricelistInactiveListings = []
breedCount4PricelistInactiveListings = []
breedCount5PricelistInactiveListings = []
breedCount6PricelistInactiveListings = []
breedCount7PricelistInactiveListings = []


masterdataActiveListings = []
masterdataActiveListingsHeader = ['Listing ID', 'Pega ID', 'Bloodline', 'Type', 'Count', 'Gender', 'Price']
        
breedCount0PricelistActiveListings = []
breedCount1PricelistActiveListings = []
breedCount2PricelistActiveListings = []
breedCount3PricelistActiveListings = []
breedCount4PricelistActiveListings = []
breedCount5PricelistActiveListings = []
breedCount6PricelistActiveListings = []
breedCount7PricelistActiveListings = []

i = 80000
error = 0

for n in range(5000): 
    marketplaceAPI = requests.get('https://api.pegaxy.io/market/listing/' + str(i))
    status = marketplaceAPI.status_code
    masterdataRaw = marketplaceAPI.text
    if status == 404 and error < 10:
        error += 1
        i += 1

    elif status == 200:
        error = 0
        parse_json = json.loads(masterdataRaw)
        listingID = parse_json['listing']['id']
        nft = parse_json['nft']
        if nft == None:
            i += 1

        else:
            pegaID = parse_json['nft']['id']
            bloodline = parse_json['nft']['bloodLine']
            breedType = parse_json['nft']['breedType']
            breedCount = parse_json['nft']['breedTime']
            gender = parse_json['nft']['gender']
            ended = parse_json['listing']['isEnded']
            seller = parse_json['listing']['owner']['address']
            buyer = parse_json['nft']['owner']['address']

            priceRaw = parse_json['listing']['price']
            currencyRaw = parse_json['listing']['currency']
            if currencyRaw == '':
                price = priceRaw[:-6]
                currency = 'USDT'
                
            else:
                price = priceRaw[:-18]
                currency = 'PGX'

            if bloodline == desiredBloodline and breedType == desiredBreedType and seller != buyer and ended == True:
                dataInactiveListings = []
                dataInactiveListings.append(str(listingID))
                dataInactiveListings.append(str(pegaID))
                dataInactiveListings.append(str(bloodline))
                dataInactiveListings.append(str(breedType))
                dataInactiveListings.append(str(breedCount))
                dataInactiveListings.append(str(gender))
                dataInactiveListings.append(str(price) + " " + str(currency))
                masterdataInactiveListings.append(dataInactiveListings)

                if breedCount == 0 and currency == 'USDT':
                    breedCount0PricelistInactiveListings.append(int(price))
                    
                if breedCount == 1 and currency == 'USDT':
                    breedCount1PricelistInactiveListings.append(int(price))
                
                if breedCount == 2 and currency == 'USDT':
                    breedCount2PricelistInactiveListings.append(int(price))
                
                if breedCount == 3 and currency == 'USDT':
                    breedCount3PricelistInactiveListings.append(int(price))
                
                if breedCount == 4 and currency == 'USDT':
                    breedCount4PricelistInactiveListings.append(int(price))

                if breedCount == 5 and currency == 'USDT':
                    breedCount5PricelistInactiveListings.append(int(price))
                
                if breedCount == 6 and currency == 'USDT':
                    breedCount6PricelistInactiveListings.append(int(price))
                
                if breedCount == 7 and currency == 'USDT':
                    breedCount7PricelistInactiveListings.append(int(price))
                

            elif bloodline == desiredBloodline and breedType == desiredBreedType and seller == buyer and ended == False:
                dataActiveListings = []
                dataActiveListings.append(str(listingID))
                dataActiveListings.append(str(pegaID))
                dataActiveListings.append(str(bloodline))
                dataActiveListings.append(str(breedType))
                dataActiveListings.append(str(breedCount))
                dataActiveListings.append(str(gender))
                dataActiveListings.append(str(price) + " " + str(currency))
                masterdataActiveListings.append(dataActiveListings)

                if breedCount == 0 and currency == 'USDT':
                    breedCount0PricelistActiveListings.append(int(price))
                    
                if breedCount == 1 and currency == 'USDT':
                    breedCount1PricelistActiveListings.append(int(price))
                
                if breedCount == 2 and currency == 'USDT':
                    breedCount2PricelistActiveListings.append(int(price))
                
                if breedCount == 3 and currency == 'USDT':
                    breedCount3PricelistActiveListings.append(int(price))
                
                if breedCount == 4 and currency == 'USDT':
                    breedCount4PricelistActiveListings.append(int(price))

                if breedCount == 5 and currency == 'USDT':
                    breedCount5PricelistActiveListings.append(int(price))

                if breedCount == 6 and currency == 'USDT':
                    breedCount6PricelistActiveListings.append(int(price))

                if breedCount == 7 and currency == 'USDT':
                    breedCount7PricelistActiveListings.append(int(price))
                
            i += 1

    else:
        break

print('Marketplace Data |', timestamp)
print('')
print('---------------------------Inactive Listings for ' + desiredBloodline + '---------------------------')
print(tabulate(masterdataInactiveListings, headers = masterdataInactiveListingsHeader, tablefmt="github"))
print('')
print('---------------------------Active Listings for ' + desiredBloodline + '---------------------------')
print(tabulate(masterdataActiveListings, headers = masterdataActiveListingsHeader, tablefmt="github"))

def average(list):
    if len(list) > 0:
        return sum(list) / len(list)
    else:
        return 0
        
breedCount0AveragePriceInactiveListings = average(breedCount0PricelistInactiveListings)
breedCount1AveragePriceInactiveListings = average(breedCount1PricelistInactiveListings)
breedCount2AveragePriceInactiveListings = average(breedCount2PricelistInactiveListings)
breedCount3AveragePriceInactiveListings = average(breedCount3PricelistInactiveListings)
breedCount4AveragePriceInactiveListings = average(breedCount4PricelistInactiveListings)
breedCount5AveragePriceInactiveListings = average(breedCount5PricelistInactiveListings)
breedCount6AveragePriceInactiveListings = average(breedCount6PricelistInactiveListings)
breedCount7AveragePriceInactiveListings = average(breedCount7PricelistInactiveListings)

print('')
print('--------------------Average Prices of ' + desiredBloodline + ' per Breedcount--------------------')
print('Breedcount 0: ' + str(breedCount0AveragePriceInactiveListings) + ' USDT in ' + str(len(breedCount0PricelistInactiveListings)) + ' sold.')
print('Breedcount 1: ' + str(breedCount1AveragePriceInactiveListings) + ' USDT in ' + str(len(breedCount1PricelistInactiveListings)) + ' sold.')
print('Breedcount 2: ' + str(breedCount2AveragePriceInactiveListings) + ' USDT in ' + str(len(breedCount2PricelistInactiveListings)) + ' sold.')
print('Breedcount 3: ' + str(breedCount3AveragePriceInactiveListings) + ' USDT in ' + str(len(breedCount3PricelistInactiveListings)) + ' sold.')
print('Breedcount 4: ' + str(breedCount4AveragePriceInactiveListings) + ' USDT in ' + str(len(breedCount4PricelistInactiveListings)) + ' sold.')
print('Breedcount 5: ' + str(breedCount5AveragePriceInactiveListings) + ' USDT in ' + str(len(breedCount5PricelistInactiveListings)) + ' sold.')
print('Breedcount 6: ' + str(breedCount6AveragePriceInactiveListings) + ' USDT in ' + str(len(breedCount6PricelistInactiveListings)) + ' sold.')
print('Breedcount 7: ' + str(breedCount7AveragePriceInactiveListings) + ' USDT in ' + str(len(breedCount7PricelistInactiveListings)) + ' sold.')

breedCount0AveragePriceActiveListings = average(breedCount0PricelistActiveListings)
breedCount1AveragePriceActiveListings = average(breedCount1PricelistActiveListings)
breedCount2AveragePriceActiveListings = average(breedCount2PricelistActiveListings)
breedCount3AveragePriceActiveListings = average(breedCount3PricelistActiveListings)
breedCount4AveragePriceActiveListings = average(breedCount4PricelistActiveListings)
breedCount5AveragePriceActiveListings = average(breedCount5PricelistActiveListings)
breedCount6AveragePriceActiveListings = average(breedCount6PricelistActiveListings)
breedCount7AveragePriceActiveListings = average(breedCount7PricelistActiveListings)

print('')
print('--------------------Average Prices of ' + desiredBloodline + ' per Breedcount--------------------')
print('Breedcount 0: ' + str(breedCount0AveragePriceActiveListings) + ' USDT in ' + str(len(breedCount0PricelistActiveListings)) + ' listed.')
print('Breedcount 1: ' + str(breedCount1AveragePriceActiveListings) + ' USDT in ' + str(len(breedCount1PricelistActiveListings)) + ' listed.')
print('Breedcount 2: ' + str(breedCount2AveragePriceActiveListings) + ' USDT in ' + str(len(breedCount2PricelistActiveListings)) + ' listed.')
print('Breedcount 3: ' + str(breedCount3AveragePriceActiveListings) + ' USDT in ' + str(len(breedCount3PricelistActiveListings)) + ' listed.')
print('Breedcount 4: ' + str(breedCount4AveragePriceActiveListings) + ' USDT in ' + str(len(breedCount4PricelistActiveListings)) + ' listed.')
print('Breedcount 5: ' + str(breedCount5AveragePriceActiveListings) + ' USDT in ' + str(len(breedCount5PricelistActiveListings)) + ' listed.')
print('Breedcount 6: ' + str(breedCount6AveragePriceActiveListings) + ' USDT in ' + str(len(breedCount6PricelistActiveListings)) + ' listed.')
print('Breedcount 7: ' + str(breedCount7AveragePriceActiveListings) + ' USDT in ' + str(len(breedCount7PricelistActiveListings)) + ' listed.')
print('')