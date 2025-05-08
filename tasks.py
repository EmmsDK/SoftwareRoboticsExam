import requests
import csv
from robocorp.tasks import task

def extract_pokemon_types(types_list):
    return ", ".join([type_info["type"]["name"] for type_info in types_list])

def fetch_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "id": data["id"],
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "types": extract_pokemon_types(data["types"])
        }
        print(f"Fetched {pokemon_info['name']} (ID {pokemon_info['id']})")
        return pokemon_info
    else:
        print(f"Failed to fetch Pokémon ID {pokemon_id}")
        return None

@task
def main():
    filename = "first_gen_pokemon.csv"
    headers = ["ID", "Name", "Height", "Weight", "Types"]

    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()

        for pokemon_id in range(1, 152):  # IDs 1 to 151
            pokemon_data = fetch_pokemon_data(pokemon_id)
            if pokemon_data:
                writer.writerow({
                    "ID": pokemon_data["id"],
                    "Name": pokemon_data["name"],
                    "Height": pokemon_data["height"],
                    "Weight": pokemon_data["weight"],
                    "Types": pokemon_data["types"]
                })

    print(f"Saved data for first generation Pokémon to {filename}")
