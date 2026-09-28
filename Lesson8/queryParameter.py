import requests

pokemon1 = input("Enter first Pokémon: ")
pokemon2 = input("Enter second Pokémon: ")

url1 = f"https://pokeapi.co/api/v2/pokemon/{pokemon1}"
url2 = f"https://pokeapi.co/api/v2/pokemon/{pokemon2}"


data1 = requests.get(url1).json()
data2 = requests.get(url2).json()

hp1 = data1["stats"][0]["base_stat"]
hp2 = data2["stats"][0]["base_stat"]

print(pokemon1, "HP:", hp1)
print(pokemon2, "HP:", hp2)


"""
What
Key / access
Example
❤️ HP
stats[0]["base_stat"]
80
⚔️ Attack
stats[1]["base_stat"]
120
🛡️ Defense
stats[2]["base_stat"]
90
✨ Special Attack
stats[3]["base_stat"]
110
🛡️ Special Defense
stats[4]["base_stat"]
80
⚡ Speed
stats[5]["base_stat"]
100
📏 Height
height
17
⚖️ Weight
weight
905
⭐ Base Experience
base_experience
270
🧬 Types
types
Fire / Flying"""
# import requests

# pokemon1 = input("tell you pokemon")

# url = f"https://pokeapi.co/api/v2/pokemon/{pokemon1}"

# res = requests.get(url)
# parse = res.json()
# # print(res.text)

# print(parse)