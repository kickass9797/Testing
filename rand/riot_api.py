#https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches1.json
#https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches2.json
#https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches3.json
#https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches4.json
#https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches5.json
#https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches6.json
#https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches7.json
#https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches8.json
#https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches9.json
#https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches10.json

import json
import requests
from urllib.request import urlopen

api_key = "RGAPI-dde45112-ac73-42d7-81f7-4b02dea56df2"

def get_Summoner(summoner, api_key):
    #loads summoner data. converts bytes to json and then to python dict
    url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner}?api_key={api_key}"
    with urlopen(url) as response:
        source = response.read().decode()
    return json.loads(source)

def get_matchlist():
    return

def get_json_url(url):
    #loads json from url.
    with requests.get(url) as response:
        data = response.json()
    return data

summoner = get_Summoner("Cloud63","RGAPI-dde45112-ac73-42d7-81f7-4b02dea56df2")
acc_ID = summoner["accountId"]
with urlopen(f"https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/{acc_ID}?api_key={api_key}") as response:
    source = response.read().decode()
matchlist = json.loads(source)
gameId_list = []
for matches in matchlist["matches"]:
    gameId_list.append(matches["gameId"])
with urlopen(f"https://euw1.api.riotgames.com/lol/match/v4/matches/{gameId_list[0]}?api_key={api_key}") as response:
    source = response.read().decode()
match = json.loads(source)
print(json.dumps(match,indent=2))















