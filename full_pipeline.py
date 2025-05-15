import subprocess

print("🔄 Starting data extraction with tasks.py...")
result1 = subprocess.run(["python", "-m", "robocorp.tasks", "run", "tasks.py"])
if result1.returncode != 0:
    print("❌ Data extraction failed.")
    exit(1)

print("✅ Data extraction complete.")

print("🔄 Running cleaning and transformation...")
result2 = subprocess.run(["python", "clean_and_transform.py"])
if result2.returncode != 0:
    print("❌ Cleaning and transformation failed.")
    exit(2)

print("✅ Full pipeline finished successfully.")

## This will:
## Fetch the data
## Clean and transform it
## Save to Excel and SQLite
## Log everything to output/*.log