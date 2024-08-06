import asyncio
from gmqtt import Client as MQTTClient
import logging
import json

logging.basicConfig(level=logging.INFO)

async def on_connect(client, flags, rc, properties):
    logging.info('Connected')
    client.subscribe('/events', qos=0)

async def on_message(client, topic, payload, qos, properties):
    message = payload.decode()
    sensor_data = json.loads(message)
    sensor_value = sensor_data["sensor_value"]
    logging.info(f"Received sensor value: {sensor_value}")
    print(f"Received sensor value: {sensor_value}")

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

if __name__ == '__main__':
    logging.info('Starting main...')
    asyncio.run(main())
    logging.info('Main finished.')