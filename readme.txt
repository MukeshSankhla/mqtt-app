MQTT Repository
This repository contains a Python application that connects to a Mosquitto MQTT broker, listens for messages on the /events topic, and prints the received sensor values.

Prerequisites
* Docker installed on your system
* Mosquitto MQTT broker running in a Docker container

Installation:
* Clone the repository from 'https://github.com/MukeshSankhla/mqtt.git'
* Extract the zip file and open a terminal
* Build the Docker composition using the command 'docker-compose build'
* Run the Docker containers in detached mode with the command 'docker-compose up -d'

Usage:
* Open the Docker Mosquitto terminal
* Manually publish a message using the command: 'mosquitto_pub -h localhost -t "/events" -m '{"sensor_value":20.2}''
* Open the mqtt_reader log to receive the values

Code Explanation:
* The mqtt_reader.py script uses the gmqtt library to connect to the Mosquitto MQTT broker and listen for messages on the /events topic. The on_message function is called when a message is received, and it prints the sensor value to the console.
* The docker-compose.yml file defines the services for the Mosquitto MQTT broker and the mqtt_reader application. The Dockerfile defines the build process for the mqtt_reader image.
