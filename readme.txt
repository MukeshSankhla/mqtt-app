To install and set up the MQTT repository, follow these steps:

1. First, install Docker on your system.
2. Next, clone the repository from https://github.com/MukeshSankhla/mqtt.git.
3. Extract the zip file and open a terminal.
4. Build the Docker composition using the command 'docker-compose build'.
5. Finally, run the Docker containers in detached mode with the 'command docker-compose up -d'.


To use the MQTT repository, follow these steps:

1. Open the Docker mosquito terminal.
2. Manually publish a message using the command: 'mosquitto_pub -h localhost -t "/events" -m '{"sensor_value":20.2}''
3. Open the mqtt_reader log to receive the values.
