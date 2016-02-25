import requests
import os
import time



def requestIngameData(region, ID, APIKey):
    time.sleep(2)
    if region == "na":
        regionmod = "NA1"
    if region == "oce":
        regionmod = "oc1"
    URL = "https://" + region + ".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/" + regionmod + "/" + ID + "?api_key=" + APIKey
    print(URL)
    responseraw = requests.get(URL)
    #print(responseraw.status_code)
    temp = (" ")
    temp = responseraw.status_code
    #print(temp)
    bad = 404
    good = 200
    if bad == temp:
        ingame = 0
        champion = 0
    elif good == temp:
        ingame = 1
        response=responseraw.json()
        
        champion = response['participants'][0]['championId']
        #champion =response['championId']
        
    return (ingame, champion)

def requestRankedData(region, ID, APIKey):
    time.sleep(2)
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    print(URL)
    responseraw = requests.get(URL)
    print(responseraw.status_code)
    response=responseraw.json()
    print(response)
    #division = response[ID][0]['entries'][0]['division']
    #lp = response[ID][0]['entries'][0]['leaguePoints']
    #tier = response[ID][0]['tier']
    #print(tier)
    #print(division)
    #print(lp)

    #tier =  response[0]['tier']
    #division =  response[0]['entries'][0]['division']
    #lp = response[0]['entries'][0]['leaguePoints']
    #print(tier)
    #print(division)
    #print(lp)
    #return (tier, division,lp)
def requestSummonerLevel(region, ID, APIKey):
    time.sleep(2)
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/" + ID + "?api_key=" + APIKey
    print(URL)
    responseraw = requests.get(URL)
    response = responseraw.json()
    #print(response)
    level = response[ID]['summonerLevel']
    #print(level)
    return(level)
temp = requestIngameData("oce", "4982605", "94fc3cea-da6f-4911-a717-77b7f3283a16" )
print(temp)
#time.sleep(2)
#temp2 =requestIngameData("na", "65499088", "94fc3cea-da6f-4911-a717-77b7f3283a16" )
#time.sleep(2)
#print (temp2)
temp3 = requestRankedData("na", "44166874", "94fc3cea-da6f-4911-a717-77b7f3283a16"  )
print (temp3)
#time.sleep(2)
#requestSummonerLevel("na", "65499088", "94fc3cea-da6f-4911-a717-77b7f3283a16" )
