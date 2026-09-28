import requests


url = "https://pokeapi.co/api/v2/pokemon/pikachu"
res = requests.get(url)
print(res.headers)