import requests

response = requests.get("https://ddragon.leagueoflegends.com/cdn/10.25.1/data/en_US/champion.json")
json = response.json()
championsDict = json['data']

champions = {}

for champion, info in championsDict.items():
	print(champion)
	if not champion in champions:



