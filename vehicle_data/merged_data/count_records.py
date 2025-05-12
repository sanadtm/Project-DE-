import glob
import json
import os

def main():
    json_files = sorted(glob.glob("2025-??-??.json"))
    total = 0

    for filename in json_files:
        try:
            with open(filename, "r") as f:
                records = json.load(f)
                count = len(records)
                total += count
                print(f"{filename}: {count} records")
        except Exception as e:
            print(f"❌ Error reading {filename}: {e}")

    print(f"\n📦 Total records across all files: {total}")

if __name__ == "__main__":
    main()

