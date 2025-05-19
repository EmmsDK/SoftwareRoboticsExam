import pandas as pd
import sqlite3
import logging
import sys
import os

# -------------------------------
# Setup logging
# -------------------------------
logging.basicConfig(
    filename="logs/clean_by_type.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------------
# Main Cleaning & Transformation Process
# -------------------------------
def main():
    if len(sys.argv) < 2:
        print("Please provide the Pokémon type to clean.")
        print("Example: rcc run -t \"Clean By Type\" -- fire")
        return

    pokemon_type = sys.argv[1].lower()
    input_file = f"data/pokemon_type_{pokemon_type}.csv"
    output_excel = f"output/pokemon_cleaned_type_{pokemon_type}.xlsx"
    output_db = f"output/pokemon_type_{pokemon_type}.db"

    if not os.path.exists(input_file):
        print(f"CSV file not found: {input_file}")
        return

    try:
        df = pd.read_csv(input_file)
        logging.info(f"CSV for type '{pokemon_type}' loaded.")

        # Capitalize names
        df["Name"] = df["Name"].str.capitalize()

        # Mark very low weight for manual review
        df["NeedsManualReview"] = df["Weight"] < 10

        # Drop rows with missing data
        df.dropna(inplace=True)

        # Extract primary/secondary type
        types_split = df["Types"].str.split(", ", expand=True)
        df["PrimaryType"] = types_split[0]
        df["SecondaryType"] = types_split[1]

        # Save to Excel
        df.to_excel(output_excel, index=False)
        logging.info(f"Cleaned Excel saved: {output_excel}")

        # Save to SQLite
        conn = sqlite3.connect(f"output/pokemon_type_{pokemon_type}.db")
        df.to_sql("pokemon", conn, if_exists="replace", index=False)
        conn.close()
        logging.info(f"Cleaned database saved: {output_db}")

        print(f"Cleaning done. Files saved to output/")

    except Exception as e:
        logging.error(f"Error cleaning data for type '{pokemon_type}': {e}")
        print(f"Cleaning failed: {e}")

# -------------------------------
# Entry point
# -------------------------------
if __name__ == "__main__":
    main()
