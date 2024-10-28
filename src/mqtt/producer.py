import time
import sys
import random
import paho.mqtt.client as paho

if __name__ == "__main__":
    client = paho.Client()
    # Connect to mqtt
    if client.connect("localhost", 1883, 60) != 0:
        print("Couldn't connect to the mqtt broker")
        sys.exit(1)
    # Topic var
    topic = 'temperature'
    while True:
        # Create the msg
        temp = random.uniform(15.0, 40.0)
        msg = temp
        # Publish the msg
        print(f'Publishing: temperature value: {msg}')
        client.publish(topic, msg, 0)
        # Wait 5 seconds and publish again
        time.sleep(1)
