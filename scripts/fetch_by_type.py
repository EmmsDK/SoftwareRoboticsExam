import sys
import requests
import csv
import logging
from time import sleep

# -------------------------------
# Setup logging
# -------------------------------
logging.basicConfig(
    filename="logs/fetch_by_type.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------------
# Get all Pokémon names by type
# -------------------------------
def get_pokemon_names_by_type(pokemon_type):
    url = f"https://pokeapi.co/api/v2/type/{pokemon_type.lower()}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [entry["pokemon"]["name"] for entry in data["pokemon"]]
    except Exception as e:
        logging.error(f"Failed to fetch Pokémon of type '{pokemon_type}': {e}")
        return []

# -------------------------------
# Get detailed data about a single Pokémon
# -------------------------------
def get_pokemon_details(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        types = ", ".join([t["type"]["name"] for t in data["types"]])
        return {
            "ID": data["id"],
            "Name": data["name"],
            "Height": data["height"],
            "Weight": data["weight"],
            "Types": types
        }
    except Exception as e:
        logging.warning(f"Failed to fetch data for {name}: {e}")
        return None

# -------------------------------
# Main entry point
# -------------------------------
def main():
    # Type should be passed using: rcc run -t "Fetch By Type" -- fire
    if len(sys.argv) < 2:
        print("Please provide a Pokémon type as an argument.")
        print("Example: rcc run -t \"Fetch By Type\" -- fire")
        return

    pokemon_type = sys.argv[1].lower()
    print(f"\nFetching Pokémon of type '{pokemon_type}'...")

    names = get_pokemon_names_by_type(pokemon_type)
    if not names:
        print(f"No Pokémon found for type '{pokemon_type}'")
        return

    output_file = f"data/pokemon_type_{pokemon_type}.csv"

    with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["ID", "Name", "Height", "Weight", "Types"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for name in names:
            details = get_pokemon_details(name)
            if details:
                writer.writerow(details)
                print(f"Fetched: {details['Name']}")
                sleep(0.5)

    print(f"\nDone! Saved data to {output_file}")

# -------------------------------
# Entry point check
# -------------------------------
if __name__ == "__main__":
    main()
