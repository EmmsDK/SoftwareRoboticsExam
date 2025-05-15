import pandas as pd
import logging
import sqlite3
from datetime import datetime

# -------------------------------
# Setup logging
# -------------------------------
logging.basicConfig(
    filename="output/cleaning.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------------
# Main Cleaning & Transformation Process
# -------------------------------
try:
    # Load the raw CSV file
    df = pd.read_csv("first_gen_pokemon.csv")
    logging.info("CSV file loaded successfully.")

    # Capitalize the first letter of each Pokémon name
    df["Name"] = df["Name"].str.capitalize()

    # Flag Pokémon with very low weight for manual review
    df["NeedsManualReview"] = df["Weight"] < 10  # e.g., Gastly, Haunter

    # Drop rows with any missing values
    df.dropna(inplace=True)

    # Split 'Types' into Primary and Secondary types
    types_split = df["Types"].str.split(", ", expand=True)
    df["PrimaryType"] = types_split[0]
    df["SecondaryType"] = types_split[1]  # NaN if no secondary type

    # Save cleaned data to Excel
    df.to_excel("output/pokemon_cleaned.xlsx", index=False)
    logging.info("Cleaned data saved to output/pokemon_cleaned.xlsx")

except Exception as e:
    logging.error(f"Error during data cleaning process: {e}")

# -------------------------------
# Optional: Save Cleaned Data to SQLite Database
# -------------------------------
try:
    conn = sqlite3.connect("output/pokemon.db")
    df.to_sql("pokemon", conn, if_exists="replace", index=False)
    conn.close()
    logging.info("Cleaned data saved to SQLite database at output/pokemon.db")
except Exception as e:
    logging.error(f"Error saving data to database: {e}")
