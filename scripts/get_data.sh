#!/bin/bash
# get_data.sh
# Grabs call logs and app stuff from an Android phone using ADB
# Run like: ./get_data.sh <device_id> <output_folder>

# Make sure we got the right inputs
if [ $# -ne 2 ]; then
    echo "Hey, I need a device ID and output folder! Like: ./get_data.sh 12345abc output/backups"
    exit 1
fi

DEVICE=$1
OUTPUT=$2
BACKUP="backup_$(date +%Y%m%d_%H%M).ab"

# Check if adb is even installed
if ! command -v adb &> /dev/null; then
    echo "Oops, ADB isn't installed. Get it with: sudo apt install android-tools-adb"
    exit 1
fi

# Make the output folder if it’s not there
mkdir -p $OUTPUT

# Let’s see if the device is connected
echo "Checking if $DEVICE is connected..."
adb -s $DEVICE devices | grep $DEVICE || { echo "Device not found! Check USB debugging."; exit 1; }

# Start the backup
echo "Pulling call logs and contacts to $OUTPUT/$BACKUP..."
adb -s $DEVICE backup -f $OUTPUT/$BACKUP -apk -shared com.android.calllog com.android.contacts

# Check if it worked
if [ $? -eq 0 ]; then
    echo "Done! Backup saved to $OUTPUT/$BACKUP"
else
    echo "Something went wrong with the backup. Check the device."
    exit 1
fi

# Kill adb server to clean up
adb kill-server
echo "All set!"
