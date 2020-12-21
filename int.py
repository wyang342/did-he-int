import requests
import matplotlib.pyplot as plt

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

data = {"champions": {}, "queueType": {}, "roleType": {}}

# Looping through to get all matches
for startIndex in range(0, 501, 100):
	beginIndex = "?beginIndex=" + str(startIndex)
	# Getting MatchList from AccountID
	getMatchList = baseUrl + "/lol/match/v4/matchlists/by-account/" + accountID + beginIndex + apiKeyAnd
	responseFromMatchList = requests.get(getMatchList)
	matchList = responseFromMatchList.json()
	matches = matchList['matches']
	for matchDict in matches:
		champion = matchDict["champion"]
		if not champion in data["champions"]:
			data["champions"][champion] = 1
		else:
			data["champions"][champion] += 1
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

# Plotting champions
x = []
y = []
for a,b in enumerate(data["champions"]):
	x.append(b)
	y.append(a)

plt.style.use('ggplot')
plt.bar(x, y, color='purple')
plt.xlabel("Champion ID")
plt.ylabel("Number of Times Played")
plt.title("Number of times champ was played")
# plt.xticks(x_pos, x)
plt.show()
