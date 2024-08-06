
# MQTT App

This repository contains a Python application that connects to a Mosquitto MQTT broker, listens for messages on the /events topic, and prints the received sensor values.

### How it Works

* The application uses the gmqtt library to connect to the Mosquitto MQTT broker.
* It subscribes to the /events topic with QoS 0.
* When a message is received on the subscribed topic, the application decodes the payload, parses the JSON data, and extracts the sensor_value.
* The application logs and prints the received sensor value.

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


### Python program
Importing Modules: The app starts by importing the necessary modules:
```bash
import asyncio
from gmqtt import Client as MQTTClient
import logging
import json
```
* asyncio for asynchronous I/O operations
* gmqtt for MQTT client functionality
* logging for logging messages
* json for parsing JSON Data

For confirming that our sensor value is being delivered we are using:
```bash
logging.basicConfig(level=logging.INFO)
```

Defining Callback Functions: The app defines two callback functions:
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
* on_connect: called when the client connects to the MQTT broker. It subscribes to the /events topic with QoS 0.
* on_message: called when a message is received on the subscribed topic. It decodes the payload, parses the JSON data, extracts the sensor_value, and logs and prints the value.

Defining the Main Function: The main function is the entry point of the app. It:
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
* Creates an MQTT client with the client ID "client-id".
* Sets up the on_connect and on_message callback functions.
* Connects to the MQTT broker at mosquitto:1883.
* Runs forever using asyncio.Future().
* When the app is interrupted, it disconnects from the MQTT broker.
Running the App:
```bash
if __name__ == '__main__':
    logging.info('Starting main...')
    asyncio.run(main())
    logging.info('Main finished.')
```
* The app is run using asyncio.run(main()), which executes the main function asynchronously.

### Docker Compose File

The docker-compose.yml file defines two services: mosquitto and mqtt_reader.

* We have set the IP of the network to the range of 172.18.0.1 to 172.18.0.254 using IP Address Management (IPAM).
* The mosquitto service uses the official Eclipse Mosquitto image and exposes ports 1883 and 9001.
* The mqtt_reader service is built from the Dockerfile in the current directory and depends on the mosquitto service.
### Dockerfile

The Dockerfile installs Python 3.12, copies the requirements.txt file, installs the required packages, copies the mqtt_reader.py file, and sets the command to run the Python script.

### Requirements

The requirements.txt file specifies the required packages:

```bash
gmqtt==0.6.9
asyncio
```
