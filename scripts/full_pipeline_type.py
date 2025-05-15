import subprocess
import sys

# -------------------------------
# Main entry point for running fetch + clean by type
# -------------------------------
def main():
    # Require type to be passed in as an argument
    if len(sys.argv) < 2:
        print("❌ Please provide a Pokémon type as an argument.")
        print("Example: rcc run -t \"Full Pipeline By Type\" -- fire")
        return

    pokemon_type = sys.argv[1].lower()

    # Step 1: Fetch
    print(f"\n🔄 Fetching Pokémon of type '{pokemon_type}'...")
    fetch = subprocess.run(["python", "scripts/fetch_by_type.py", pokemon_type])
    if fetch.returncode != 0:
        print("❌ Failed during fetching.")
        return

    # Step 2: Clean
    print(f"\n🧹 Cleaning data for type '{pokemon_type}'...")
    clean = subprocess.run(["python", "scripts/clean_type_data.py", pokemon_type])
    if clean.returncode != 0:
        print("❌ Failed during cleaning.")
        return

    print(f"\n✅ Full pipeline for type '{pokemon_type}' completed successfully!")

# -------------------------------
# Execute if run directly
# -------------------------------
if __name__ == "__main__":
    main()
