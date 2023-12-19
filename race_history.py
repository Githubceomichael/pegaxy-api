import requests
import json

dataFinal = []
metamaskAddress = ''

masterdata = requests.get('https://api-apollo.pegaxy.io/v1/pegas/owner/user/' + str(metamaskAddress))
masterdataText = masterdata.text
masterdataParsed = json.loads(masterdataText)

id = [x['id'] for x in masterdataParsed]
i = 0
print(id)
print(len(id))

for n in range(len(id)):
    print(id[i])
    racingData = requests.get('https://api-apollo.pegaxy.io/v1/game-api/race/history/pega/' + str(id[i]))
    racingDataText = racingData.text
    racingDataParsed = json.loads(racingDataText)
    
    i += 1