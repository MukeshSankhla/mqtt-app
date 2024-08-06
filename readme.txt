To install and set up the MQTT repository, follow these steps:

First, install Docker on your system.
Next, clone the repository from https://github.com/MukeshSankhla/mqtt.git.
Extract the zip file and open a terminal.
Build the Docker composition using the command docker-compose build.
Finally, run the Docker containers in detached mode with the command docker-compose up -d.



mosquitto_pub -h localhost -t "/events" -m '{"sensor_value":20.2}'
