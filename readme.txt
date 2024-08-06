
# MQTT App

## MQTT Repository
This repository contains a Python application that connects to a Mosquitto MQTT broker, listens for messages on the /events topic, and prints the received sensor values.

### Prerequisites
* Docker installed on your system
* Mosquitto MQTT broker running in a Docker container

### Installation:
* Clone the repository from 'https://github.com/MukeshSankhla/mqtt.git'
* Extract the zip file and open a terminal
* Build the Docker composition using the command 'docker-compose build'
* Run the Docker containers in detached mode with the command 'docker-compose up -d'

![](https://github.com/MukeshSankhla/mqtt/blob/main/images/Screenshot%202024-08-06%20201629.png)
![](https://github.com/MukeshSankhla/mqtt/blob/main/images/Screenshot%202024-08-06%20201652.png)
![](https://github.com/MukeshSankhla/mqtt/blob/main/images/Screenshot%202024-08-06%20202810.png)

### Usage:
* Open the Docker Mosquitto terminal by using windows comand prompt 'docker exec -it mqtt-main-mosquitto-1 sh'.
* Manually publish a message using the command: 'mosquitto_pub -h localhost -t "/events" -m '{"sensor_value":20.2}''.
* Open the mqtt_reader log to receive the values.
![](https://github.com/MukeshSankhla/mqtt/blob/main/images/Screenshot%202024-08-06%20202748.png)

### Code Explanation:
* The mqtt_reader.py script uses the gmqtt library to connect to the Mosquitto MQTT broker and listen for messages on the /events topic. The on_message function is called when a message is received, and it prints the sensor value to the console.
* The docker-compose.yml file defines the services for the Mosquitto MQTT broker and the mqtt_reader application. The Dockerfile defines the build process for the mqtt_reader image.


```bash
import asyncio
from gmqtt import Client as MQTTClient
import logging
import json

logging.basicConfig(level=logging.INFO)
```


```bash
async def on_connect(client, flags, rc, properties):
    logging.info('Connected')
    client.subscribe('/events', qos=0)

async def on_message(client, topic, payload, qos, properties):
    message = payload.decode()
    sensor_data = json.loads(message)
    sensor_value = sensor_data["sensor_value"]
    logging.info(f"Received sensor value: {sensor_value}")
    print(f"Received sensor value: {sensor_value}")
```


```bash
async def main():
    logging.info('Creating MQTT client...')
    client = MQTTClient("client-id")

    logging.info('Setting up on_connect callback...')
    client.on_connect = lambda client, flags, rc, properties: asyncio.create_task(on_connect(client, flags, rc, properties))
    logging.info('Setting up on_message callback...')
    client.on_message = lambda client, topic, payload, qos, properties: asyncio.create_task(on_message(client, topic, payload, qos, properties))

    logging.info('Connecting to MQTT broker...')
    await client.connect('mosquitto', port=1883)
    logging.info('Connected to MQTT broker!')

    try:
        logging.info('Running forever...')
        await asyncio.Future()  # Run forever
    finally:
        logging.info('Disconnecting from MQTT broker...')
        await client.disconnect()
        logging.info('Disconnected from MQTT broker.')
```
```bash
if __name__ == '__main__':
    logging.info('Starting main...')
    asyncio.run(main())
    logging.info('Main finished.')
```
