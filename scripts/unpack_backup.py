#!/usr/bin/env python3
# unpack_backup.py
# Takes an ADB backup (.ab) and unpacks it using ABE
# Run: python3 unpack_backup.py <backup_file> <output_dir>

import subprocess
import os
import sys

# Quick check for inputs
if len(sys.argv) != 3:
    print("Need two args: backup file and output dir")
    print("Example: python3 unpack_backup.py data/backups/backup_20250514_1542.ab data/extracted")
    sys.exit(1)

backup_file = sys.argv[1]
output_dir = sys.argv[2]

# Make sure abe.jar is here
if not os.path.exists("abe.jar"):
    print("Can't find abe.jar! Download it from SourceForge and put it in the project folder.")
    sys.exit(1)

# Create output dir
os.makedirs(output_dir, exist_ok=True)

# Convert .ab to .tar
tar_file = os.path.join(output_dir, "backup.tar")
print(f"Converting {backup_file} to {tar_file}...")
subprocess.run(["java", "-jar", "abe.jar", "unpack", backup_file, tar_file])

# Extract the tar
extracted_dir = os.path.join(output_dir, "extracted")
os.makedirs(extracted_dir, exist_ok=True)
print(f"Unpacking tar to {extracted_dir}...")
subprocess.run(["tar", "-xvf", tar_file, "-C", extracted_dir])

print("All done! Check", extracted_dir, "for the data.")
