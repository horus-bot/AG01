from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return {
        "greet":"hey from the sg"
    }

@app.get("hey")
def yo():
    return {
        "yo":"hello"
    }

@app.get("/names")
def pokemon_names(name:str):
    resp = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    data = resp.json()
    return {
        "name": data["name"],
        "health": data["stats"][0]["base_stat"],
        "height": data["height"],
        "weight": data["weight"]
    }



@app.get("/pokemon/{name}/moves")
def pokemon_moves(name: str):

    resp = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{name}"
    )

    data = resp.json()

    moves = data["moves"][:2]

    result = []

    for move in moves:

        move_name = move["move"]["name"]

        move_resp = requests.get(
            f"https://pokeapi.co/api/v2/move/{move_name}"
        )

        move_data = move_resp.json()

        result.append({
            "name": move_data["name"],
            "power": move_data["power"]
        })

    return {
        "pokemon": data["name"],
        "moves": result
    }