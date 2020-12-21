import requests
import matplotlib.pyplot as plt
import champions

# Getting API key
handle = open("api-key.txt", "r")
api_key = handle.read()
apiKeyQuestion = "?api_key=" + api_key
apiKeyAnd = "&api_key=" + api_key

# URLS
baseUrl = "https://na1.api.riotgames.com"
getSummonerByName = baseUrl + "/lol/summoner/v4/summoners/by-name/hyeonipus" + apiKeyQuestion

# Getting accountID from summoner name
responseFromSummonerName = requests.get(getSummonerByName)
dataFromSummonerName = responseFromSummonerName.json()
accountID = dataFromSummonerName['accountId']

# Initializing data to be collected
data = {"champions": {}, "queueType": {}, "roleType": {}}

# Looping through to get all matches
for startIndex in range(0, 501, 100):
	beginIndex = "?beginIndex=" + str(startIndex)
	# Getting MatchList from AccountID
	getMatchList = baseUrl + "/lol/match/v4/matchlists/by-account/" + accountID + beginIndex + apiKeyAnd
	responseFromMatchList = requests.get(getMatchList)
	matchList = responseFromMatchList.json()
	matches = matchList['matches'] # list of match dictionaries
	for matchDict in matches:
		champion = str(matchDict["champion"])
		championName = champions.champions_inverted[champion]
		if not championName in data["champions"]:
			data["champions"][championName] = 1
		elif championName in data['champions']:
			data["champions"][championName] += 1
		queue = matchDict["queue"]
		if not queue in data["queueType"]:
			data["queueType"][queue] = 1
		else:
			data["queueType"][queue] += 1
		role = matchDict["role"]
		if not role in data["roleType"]:
			data["roleType"][role] = 1
		else:
			data["roleType"][role] += 1

# Plotting champion data
x = []
y = []
for a, b in data["champions"].items():
	x.append(a)
	y.append(b)

plt.style.use('ggplot')
plt.barh(x, y, color='purple')
plt.xlabel("# of Games Played")
plt.ylabel("Champion Name")
plt.title("# of Times Each Champion was Played")
plt.show()
