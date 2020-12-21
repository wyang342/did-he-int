import requests

response = requests.get("https://ddragon.leagueoflegends.com/cdn/10.25.1/data/en_US/champion.json")
json = response.json()
championsDict = json['data']

champions = {}

for champion, info in championsDict.items():
	if not champion in champions:
		champions[champion] = championsDict[champion]['key']

champions_inverted = {v: k for k, v in champions.items()}
