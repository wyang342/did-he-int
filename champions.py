import requests

response = requests.get("https://ddragon.leagueoflegends.com/cdn/10.25.1/data/en_US/champion.json")
champions = response.json()

print(champions['data'])

for