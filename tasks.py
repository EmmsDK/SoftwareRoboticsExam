from robocorp.tasks import task

import requests

def fetch_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name']}")
        print(f"ID: {data['id']}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
    else:
        print("Failed to fetch Pokémon data")

# The main function Robocorp uses as the default task:
@task
def main():
    fetch_pokemon()
