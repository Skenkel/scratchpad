import requests
import os
def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    print(URL)
    response = requests.get(URL)
    tier =  response[0]['tier']
    division =  response[0]['entries'][0]['division']
    lp = response[0]['entries'][0]['leaguePoints']
    return (tier, division, lp)
def requestIngameData(region, ID, APIKey):
    if region = "na":
        regionmod = "NA1"
    if region = "oce":
        regionmod = "oc1"
        

    URL = "https://" + region + ".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/" + regionmod + "/" + ID + "?api_key=" + APIKey
    print(URL)
    response = requests.get(URL)
    tier =  response[0]['tier']
    return (tier, division, lp)
def requestSummonerLevel(region, ID, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/" + ID + "/entry?api_key=" + APIKey
    print(URL)
    response = requests.get(URL)
    tier =  response[0]['tier']
    division =  response[0]['entries'][0]['division']
    lp = response[0]['entries'][0]['leaguePoints']
    return (tier, division, lp)
# first we get our non changing data
apikeyraw = open('apikey.txt')
apikey = apikeyraw.read()
num_summoners = sum(1 for line in open('summoners.txt'))
print(num_summoners)
summonersraw = open("summoners.txt")
#print(apikey)
summonerstaticlist = []
#print(summonersraw.readline())
#print(summonersraw.readline())
#go through the file line by line creating a list for each summoner name, and then adding all to one list      
for tempiter in range(0, num_summoners):
    print(summonersraw.readline(tempiter))
    summonerstatic = []
    summonerstatic = summonersraw.readline().split()
    summonerstaticlist.insert(tempiter,summonerstatic)
    print(summonerstaticlist)
#print(summonerlist)
#print(summonerlist[1][0])
# next we create the infinite loop that keeps going

while true
    # we are creating a list for each summoner with a static key for variables: ingame(0/1), currentlyplaying, level,  league, division, lp
    summonerdynamiclist = []
    for tempiter in range(0, num_summoners):
        summonerdynamic = []
        summonerdynamic.append()
        summonerdynamiclist.insert(tempiter,summonerdynamic)
# Now we print out our results
    for tempiter in range(0, num_summoners):
        if summonerdynamiclist[tempiter[0]] == 0:
                               print("Sam's", summonerstaticlist[tempiter][1]) ,'is not in game right now. The account is level',summonerdynamiclist[tempiter[2]] ,"In the",summonerdynamiclist[tempiter[3]] , "league, division",summonerdynamiclist[tempiter[4]] , "with",summonerdynamiclist[tempiter[5]] ,"lp")
        else:
            print("Sam's", summonerstaticlist[tempiter][1]) ,' is in game right now. He is playing champion',summonerdynamiclist[tempiter[1]] , 'The account is level',summonerdynamiclist[tempiter[2]] ,"In the",summonerdynamiclist[tempiter[3]] , "league, division",summonerdynamiclist[tempiter[4]] , "with",summonerdynamiclist[tempiter[5]] ,"lp")

                              
                               
    


for tempiter in range(0, num_summoners):



#with open('summoners.txt') as f:
#    temp = 0
#    for line in f:
#        print(f.readlines(temp))
#        summonerlist.append(f.readline())
#        temp = temp+1
#print(summonerlist[0])

#with open('summoners.txt') as f:
#    summonerlines = f.readlines()
   
