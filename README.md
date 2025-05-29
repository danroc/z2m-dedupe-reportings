# Zigbee2MQTT Reporting Dedupe Tool

A Python small script to remove duplicate reporting entries from the
Zigbee2MQTT database.

## Usage

1. Download the script:

   ```bash
   wget https://raw.githubusercontent.com/danroc/z2m-dedupe-reportings/refs/heads/main/dedupe.py
   ```

2. Stop Zigbee2MQTT

   ```bash
   docker stop zigbee2mqtt
   ```

3. Backup the database

   ```bash
   cp database.db database.db.bak
   ```

4. Run the dedupe tool

   ```bash
   python3 dedupe.py database.db.bak -o database.db
   ```

5. Start Zigbee2MQTT

   ```bash
   docker start zigbee2mqtt
   ```
