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
getSummonerByName = baseUrl + "/lol/summoner/v4/summoners/by-name/jyuan16" + apiKeyQuestion

# Getting accountID from summoner name
responseFromSummonerName = requests.get(getSummonerByName)
dataFromSummonerName = responseFromSummonerName.json()
accountID = dataFromSummonerName['accountId']

# Initializing data to be collected
data = {"champions": {}, "queueType": {}, "roleType": {}}

# Looping through to get all matches
startIndex = 0
while True:
	beginIndex = "?beginIndex=" + str(startIndex)
	# Getting MatchList from AccountID
	getMatchList = baseUrl + "/lol/match/v4/matchlists/by-account/" + accountID + beginIndex + apiKeyAnd
	responseFromMatchList = requests.get(getMatchList)
	matchList = responseFromMatchList.json()
	try:
		matches = matchList['matches']  # list of match dictionaries
	except:
		print("Can't Retrieve Data")
		break;
	if not matches:
		break;
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
	startIndex += 100;

# Plotting champion data
champ_name = []
num_played = []
for a, b in data["champions"].items():
	champ_name.append(a)
	num_played.append(b)

# Listing Champions in Alphabetical order
zipped_list = zip(champ_name, num_played)
sorted_zipped_list = sorted(zipped_list)
sorted_zipped_list.reverse()

sorted_list = [[i for i, j in sorted_zipped_list], [j for i, j in sorted_zipped_list]]
plt.style.use('ggplot')
plt.figure(1, figsize=(9, 20))
plt.barh(sorted_list[0], sorted_list[1], color='blue')
plt.xlabel("# of Games Played")
plt.ylabel("Champion Name")
plt.title("# of Times Each Champion was Played")
plt.show()


print("done")