import requests
import os
import time



def requestIngameData(region, ID, APIKey):
    time.sleep(2)
    regionmod = ""
    if region == "na":
        regionmod = "NA1"
    if region == "oce":
        regionmod = "oc1"
    URL = "https://" + region + ".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/" + regionmod + "/" + ID + "?api_key=" + APIKey
    #print(URL)
    responseraw = requests.get(URL)
    #print(responseraw.status_code)
    temp = (" ")
    temp = responseraw.status_code
    #print(temp)
    bad = 404
    good = 200
    ingame = 0
    champion = 0
    if bad == temp:
        ingame = 0
        champion = 0
    if good == temp:
        ingame = 1
        response=responseraw.json()
        
        champion = response['participants'][0]['championId']
    return (ingame , champion)
        #champion =response['championId']
        
    #return (ingame, champion)

def requestRankedData(region, ID, APIKey):
    time.sleep(2)
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    #print(URL)
    
    responseraw = requests.get(URL)
    status = responseraw.status_code
    #print(status)
    good = 200
    bad = 404
    ranked = 0
    tier = "unranked"
    division = "unranked"
    lp = "unranked"
    if status == bad:
        ranked = 0
        tier = "unranked"
        division = "unranked"
        lp = "unranked"
    if status == good:
        response=responseraw.json()
        #print(response)
        division = response[ID][0]['entries'][0]['division']
        lp = response[ID][0]['entries'][0]['leaguePoints']
        tier = response[ID][0]['tier']
        ranked = 1
    return (tier, division,lp, ranked)
    #print(tier)
    #print(division)
    #print(lp)

    #tier =  response[0]['tier']
    #division =  response[0]['entries'][0]['division']
    #lp = response[0]['entries'][0]['leaguePoints']
    #print(tier)
    #print(division)
    #print(lp)
    #return (tier, division,lp, ranked)
def requestSummonerLevel(region, ID, APIKey):
    time.sleep(2)
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/" + ID + "?api_key=" + APIKey
    #print(URL)
    responseraw = requests.get(URL)
    response = responseraw.json()
    #print(response)
    level = response[ID]['summonerLevel']
    #print(level)
    return(level)


# first we get our non changing data
apikeyraw = open('apikey.txt')
apikey = apikeyraw.read()
num_summoners = sum(1 for line in open('summoners.txt'))
#print(num_summoners)
summonersraw = open("summoners.txt")
#print(apikey)
summonerstaticlist = []
#print(summonersraw.readline())
#print(summonersraw.readline())
#go through the file line by line creating a list for each summoner name, and then adding all to one list      
for tempiter in range(0, num_summoners):
    #print(summonersraw.readline(tempiter))
    summonerstatic = []
    summonerstatic = summonersraw.readline().split()
    summonerstaticlist.insert(tempiter,summonerstatic)
    #print(summonerstaticlist)
#print(summonerlist)
#print(summonerlist[1][0])
# next we create the infinite loop that keeps going

while True:
    #os.system('cls')
    # we are creating a list for each summoner with a static key for variables: ingame(0/1), currentlyplaying, level,  league, division, lp, ranked v unranked
    summonerdynamiclist = []
    for tempiter in range(0, num_summoners):
        
        summonerdynamic = []
        #print( summonerstaticlist[tempiter][3])
        #print(summonerstaticlist[tempiter][0])
        #print(requestIngameData(summonerstaticlist[tempiter][3], summonerstaticlist[tempiter][0], apikey))
        cursumingame = requestIngameData(summonerstaticlist[tempiter][3], summonerstaticlist[tempiter][0], apikey)[0]
        cursumchamp = requestIngameData(summonerstaticlist[tempiter][3], summonerstaticlist[tempiter][0], apikey)[1]
        cursumlevel = requestSummonerLevel(summonerstaticlist[tempiter][3], summonerstaticlist[tempiter][0], apikey)
        cursumtier = requestRankedData(summonerstaticlist[tempiter][3], summonerstaticlist[tempiter][0], apikey)[0]
        cursumdivision = requestRankedData(summonerstaticlist[tempiter][3], summonerstaticlist[tempiter][0], apikey)[1]
        cursumlp = requestRankedData(summonerstaticlist[tempiter][3], summonerstaticlist[tempiter][0], apikey)[2]
        cursumranked = requestRankedData(summonerstaticlist[tempiter][3], summonerstaticlist[tempiter][0], apikey)[3]
        #now we have the variables for our current summoner; were'going to put them into a list
        summonerdynamic.append(cursumingame)
        summonerdynamic.append(cursumchamp)
        summonerdynamic.append(cursumlevel)
        summonerdynamic.append(cursumtier)
        summonerdynamic.append(cursumdivision)
        summonerdynamic.append(cursumlp)
        summonerdynamic.append(cursumranked)
        #and now we add our list to our list
        summonerdynamiclist.insert(tempiter,summonerdynamic)
        #print(summonerdynamic)
# Now we print out our results
    for tempiter in range(0, num_summoners):
        #print(summonerdynamiclist)
        if summonerdynamiclist[tempiter][0] == 0:
            #print("at least one account is in game")

            #message = "Sam's"+ repr(summonerstaticlist[tempiter][1])) + 'is not in game right now. The account is level'+repr(summonerdynamiclist[tempiter[2]])+"In the"+repr(summonerdynamiclist[tempiter[3]]) +"league, division"+repr(summonerdynamiclist[tempiter[4]]) + "with"+ repr(summonerdynamiclist[tempiter[5]]) +"lp")
            if summonerdynamiclist[tempiter][6] == 1:
                message = "Sam's" + repr(summonerstaticlist[tempiter][2]) + "account is not in game right now. The account is level" + repr(summonerdynamiclist[tempiter][2])+ "and is in the" + repr(summonerdynamiclist[tempiter][3])+ repr(summonerdynamiclist[tempiter][2])+ "and is in the" + repr(summonerdynamiclist[tempiter][3])+ "league, division" + repr(summonerdynamiclist[tempiter][4])+ "with" + repr(summonerdynamiclist[tempiter][5])+"lp"
                print(message)
                print("\n")

            else:
                 message = "Sam's" + repr(summonerstaticlist[tempiter][2]) + "account is not in game right now. The account is level" + repr(summonerdynamiclist[tempiter][2]) + "and is unranked"
                 print(message)
                 print("\n")
        else:
            if summonerdynamiclist[tempiter][6] == 1:
                message = "Sam's" + repr(summonerstaticlist[tempiter][2]) + "account is in game right now. Playin champion id" +repr(summonerdynamiclist[tempiter][1])+ "The account is level" + repr(summonerdynamiclist[tempiter][2])+ "and is in the" + repr(summonerdynamiclist[tempiter][3])+ "league, division" + repr(summonerdynamiclist[tempiter][4])+ "with" + repr(summonerdynamiclist[tempiter][5])+"lp" 
                print(message)
                print("\n")

            else:
                 message = "Sam's" + repr(summonerstaticlist[tempiter][2]) + "account is not in game right now. The account is level" + repr(summonerdynamiclist[tempiter][2]) + "and is unranked"
                 print(message)
                 print("\n")
            #print("Sam's"+ summonerstaticlist[tempiter][1]) +' is in game right now. He is playing champion with id'+summonerdynamiclist[tempiter[1]] + 'The account is level'+summonerdynamiclist[tempiter[2]] +"In the"+summonerdynamiclist[tempiter[3]] + "league, division"+summonerdynamiclist[tempiter[4]] + "with"+summonerdynamiclist[tempiter[5]] +"lp")
