import time
import sys

import paho.mqtt.client as paho

if __name__ == "__main__":
    client = paho.Client()
    # Connect to mqtt
    if client.connect("localhost", 1883, 60) != 0:
        print("Couldn't connect to the mqtt broker")
        sys.exit(1)
    # Topic var
    topic = 'mytopic'
    while True:
        # Create the msg
        msg = f'Current time is {time.time()}'
        # Publish the msg
        print(f'Publishing: {msg}')
        client.publish(topic, msg, 0)
        # Wait 5 seconds and publish again
        time.sleep(5)
