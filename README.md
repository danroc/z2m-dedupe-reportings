# Zigbee2MQTT Reporting Dedupe Tool

A Python small script to remove duplicate reporting entries from the
Zigbee2MQTT database.

## Usage

1. Stop Zigbee2MQTT

   ```bash
   docker stop zigbee2mqtt
   ```

2. Backup the database

    ```bash
    cp database.db database.db.bak
    ```

3. Run the dedupe tool

    ```bash
    python3 dedupe.py database.db.bak -o database.db
    ```

4. Start Zigbee2MQTT

    ```bash
    docker start zigbee2mqtt
    ```
