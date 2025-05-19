## Project: Pokémon Data Automation

This project automates the retrieval and processing of Pokémon data from the public PokeAPI.  
It supports fetching either the full first generation (Gen1) or filtering by specific types (e.g., Fire, Grass).  
The data is cleaned, validated, and saved into Excel sheets and SQLite databases for further analysis or reporting.

### Use Case

Imagine a data analyst needing structured and clean Pokémon data for analytics or reporting in Excel/Power BI.  
Instead of manually scraping or copying data from a website, this robot automates:

- Fetching data from the PokeAPI.
- Cleaning and transforming the dataset.
- Saving the result into Excel and SQLite formats.
- Logging and error handling for reliability.

This pipeline reduces manual work and ensures up-to-date Pokémon data on demand.

### Available Tasks

- `Fetch Gen1`: Retrieves all 151 first-generation Pokémon and saves as CSV.
- `Clean Gen1 Data`: Cleans and transforms Gen1 data, saving to Excel and SQLite.
- `Full Pipeline Gen1`: Runs both fetch and clean steps for Gen1 Pokémon.
- `Fetch By Type`: Fetches Pokémon based on a specific type (e.g., "fire", "water").
- `Clean By Type`: Cleans and saves Pokémon of a specific type.
- `Full Pipeline Type`: Fetches and cleans data by type in one step.

### Output Files

- `data/`: Raw CSV files (`pokemon_gen1.csv`, `pokemon_type_<type>.csv`)
- `output/`: Clean Excel and SQLite databases (`pokemon_gen1_cleaned.xlsx`, `pokemon_type_<type>.db`)
- `logs/`: Log files capturing runtime details, API errors, and debug messages

###  How to Run

Use `rcc` to execute the different tasks defined in your `robot.yaml`. Below are the available pipelines and how to run them. 
You can also manually run them using the Robo corp extension.

---

####  Full Gen1 Pipeline
Fetches and cleans all first-generation Pokémon (IDs 1–151), then stores the cleaned data in both Excel and SQLite formats.

```bash
rcc run -t "Full Pipeline Gen1" 
```

#### Full Type-Based Pipeline
Fetches and cleans all Pokémon of a specified type (e.g., fire, grass, water), then stores the cleaned data in both Excel and SQLite.

```bash
rcc run -t "Full Pipeline By Type" -- fire
```

#### Fetch Gen1 Data Only
Only performs data extraction for Gen1 Pokémon and saves it to a CSV file (data/pokemon_gen1.csv).

```bash
rcc run -t "Fetch Gen1"
```

#### Clean Gen1 Data Only
Reads the raw CSV for Gen1 and performs data cleaning, then saves the cleaned output to Excel and SQLite.

```bash
rcc run -t "Clean Gen1"
```

#### Fetch Pokémon by Type Only
Fetches raw Pokémon data based on type (e.g., grass, electric, water) and saves it as a CSV in the data/ folder.

```bash
rcc run -t "Fetch By Type" -- grass
```

#### Clean Pokémon by Type Only
Reads a previously fetched type-based CSV and performs cleaning, outputting Excel and database files to output/.

```bash
rcc run -t "Clean By Type" -- electric
```
