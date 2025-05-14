#!/usr/bin/env python3
# make_report.py
# Puts together a simple HTML report from call logs
# Run: python3 make_report.py <call_logs_file> <output_dir>

import sys
import os
from datetime import datetime

# Check args
if len(sys.argv) != 3:
    print("Need call logs file and output dir. Example:")
    print("python3 make_report.py data/reports/call_logs.txt data/reports")
    sys.exit(1)

logs_file = sys.argv[1]
output_dir = sys.argv[2]

# Make sure the logs file exists
if not os.path.exists(logs_file):
    print("Call logs file doesn't exist! Check the path.")
    sys.exit(1)

# Read the logs
with open(logs_file, "r") as f:
    logs = f.readlines()

# Create the report
os.makedirs(output_dir, exist_ok=True)
report_file = os.path.join(output_dir, f"report_{datetime.now().strftime('%Y%m%d_%H%M')}.html")
with open(report_file, "w") as f:
    f.write("""
<html>
<head>
    <title>Forensic Report</title>
    <style>
        body { font-family: Arial; margin: 20px; }
        h1 { color: navy; }
        pre { background: #eee; padding: 10px; }
    </style>
</head>
<body>
    <h1>Mobile Forensics Report</h1>
    <p>Generated on: """ + datetime.now().strftime("%Y-%m-%d %H:%M") + """</p>
    <h2>Call Logs</h2>
    <pre>""" + "".join(logs) + """</pre>
    <p>Note: Autopsy report should be viewed separately.</p>
</body>
</html>
""")

print("Report saved to", report_file)
print("Looks good, but check it in a browser!")
