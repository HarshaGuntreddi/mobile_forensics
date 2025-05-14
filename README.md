Mobile Forensics Project
Hey there! This is my mobile forensics project for pulling and analyzing data from Android phones (non-rooted). I built it on Kali Linux using ADB, Android Backup Extractor (ABE), and Autopsy. It’s been a fun challenge, and I learned a ton about forensic workflows. Hope you find it useful!
What It Does

Grabs call logs and app data with ADB.
Unpacks .ab backups with ABE.
Digs into SQLite databases for call logs.
Makes a simple HTML report.
Reminds you to run Autopsy manually (yeah, I didn’t automate that part yet).

Stuff You Need

Kali Linux (I used it in VirtualBox)
ADB (sudo apt install android-tools-adb)
ABE (grab abe.jar from SourceForge)
Autopsy (get it from sleuthkit.org)
Python 3
Java (JDK 8 or 11 works)
An Android phone with USB debugging on

How to Use
Check out docs/how_to_use.txt for the step-by-step. Basically:

Extract data with get_data.sh.
Unpack it with unpack_backup.py.
Analyze with dig_data.py.
Make a report with make_report.py.

Notes

Make sure your phone trusts your computer for ADB.
I had some Java version issues; JDK 11 worked best for me.
Autopsy is manual for now—open it and point it to the extracted data.
Check notes.txt for my random thoughts and fixes.

Ethics
Only use this on devices you own or have permission to mess with. Forensics is serious stuff—don’t break laws or invade privacy!
License
MIT License (see LICENSE.txt). Feel free to use or tweak this, just give me a shout if it’s helpful!
To-Do

Automate Autopsy integration.
Maybe add some charts for call logs.
Clean up the scripts a bit.

Hit me up on GitHub if you have ideas or run into issues!

