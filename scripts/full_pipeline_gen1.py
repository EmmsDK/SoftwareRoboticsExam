import subprocess

print("🔄 Starting data extraction with Robocorp task...")
result1 = subprocess.run(["rcc", "run", "-t", "Fetch Gen1"])
if result1.returncode != 0:
    print("❌ Data extraction failed.")
    exit(1)

print("✅ Data extraction complete.")

print("🔄 Running cleaning and transformation...")
result2 = subprocess.run(["python", "scripts/clean_gen1_data.py"])
if result2.returncode != 0:
    print("❌ Cleaning and transformation failed.")
    exit(2)

print("✅ Full pipeline finished successfully.")


## This will:
## Fetch the data of gen 1
## Clean and transform it
## Save to Excel and SQLite
## Log everything to output/*.log