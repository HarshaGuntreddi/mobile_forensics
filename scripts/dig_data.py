#!/usr/bin/env python3
# dig_data.py
# Digs into the extracted data, pulls call logs from SQLite
# Note: Autopsy part is manual for now, just prints a reminder
# Run: python3 dig_data.py <data_dir> <output_dir>

import sqlite3
import os
import sys

if len(sys.argv) != 3:
    print("Gimme the extracted data dir and an output dir!")
    print("Like: python3 dig_data.py data/extracted data/reports")
    sys.exit(1)

data_dir = sys.argv[1]
output_dir = sys.argv[2]

# Make output dir
os.makedirs(output_dir, exist_ok=True)

# Look for contacts2.db (common for call logs)
db_path = os.path.join(data_dir, "extracted/apps/com.android.providers.contacts/db/contacts2.db")
if not os.path.exists(db_path):
    print("Can't find contacts2.db. Did the backup include it?")
    sys.exit(1)

# Pull call logs
print("Querying call logs...")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT number, date, duration, type FROM calls")
logs = cursor.fetchall()
conn.close()

# Save to a file
output_file = os.path.join(output_dir, "call_logs.txt")
with open(output_file, "w") as f:
    for log in logs:
        f.write(f"Number: {log[0]}, Date: {log[1]}, Duration: {log[2]}, Type: {log[3]}\n")

print("Call logs saved to", output_file)

# Reminder for Autopsy
print("Run Autopsy manually on", data_dir, "and save the report to", output_dir)
print("I haven't automated Autopsy yet, sorry!")
