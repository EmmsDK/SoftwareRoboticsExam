import os
import requests
import csv
import logging
from robocorp.tasks import task

# -------------------------------
# Ensure directories exist
# -------------------------------
os.makedirs("data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# -------------------------------
# Setup logging
# -------------------------------
logging.basicConfig(
    filename="logs/data_extraction.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------------
# Utility: Check if API is Available
# -------------------------------
def is_api_available():
    try:
        test_url = "https://pokeapi.co/api/v2/pokemon/1"
        response = requests.get(test_url, timeout=5)
        if response.status_code == 200:
            logging.info("PokeAPI is reachable.")
            return True
        else:
            logging.error(f"PokeAPI reachable but returned status {response.status_code}")
            return False
    except Exception as e:
        logging.error(f"API check failed: {e}")
        return False

# -------------------------------
# Extract Pokémon types
# -------------------------------
def extract_pokemon_types(types_list):
    return ", ".join([type_info["type"]["name"] for type_info in types_list])

# -------------------------------
# Fetch Pokémon by ID with error handling
# -------------------------------
def fetch_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "id": data["id"],
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"],
                "types": extract_pokemon_types(data["types"])
            }
        else:
            logging.warning(f"Failed to fetch ID {pokemon_id} — Status code: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Error fetching ID {pokemon_id}: {e}")
        return None

# -------------------------------
# Robocorp Task: Run Data Extraction
# -------------------------------
@task
def main():
    if not is_api_available():
        print("API not available. Aborting data extraction.")
        logging.error("Aborted task due to API being unreachable.")
        return

    filename = "data/pokemon_gen1.csv"
    headers = ["ID", "Name", "Height", "Weight", "Types"]

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
            logging.info(f"Opened {filename} for writing.")
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()

            for pokemon_id in range(1, 152):
                pokemon_data = fetch_pokemon_data(pokemon_id)
                if pokemon_data:
                    writer.writerow({
                        "ID": pokemon_data["id"],
                        "Name": pokemon_data["name"],
                        "Height": pokemon_data["height"],
                        "Weight": pokemon_data["weight"],
                        "Types": pokemon_data["types"]
                    })

            logging.info("All data written to CSV successfully.")
            print(f"Data extraction complete. File saved as {filename}")

    except PermissionError as e:
        logging.error(f"Permission denied: {e}")
        print("File is in use. Please close Excel or any program using the CSV and try again.")
    except Exception as e:
        logging.error(f"Critical error during data extraction: {e}")
        print("Failed to complete data extraction.")
