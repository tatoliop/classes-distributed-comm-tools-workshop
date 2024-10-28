import sys

import paho.mqtt.client as paho


def message_handling(client, userdata, msg):
    print(f"Subscribed to topic <{msg.topic}> and consumed msg: <{msg.payload.decode()}>")


if __name__ == "__main__":
    # Connect to mqtt
    client = paho.Client()
    client.on_message = message_handling
    if client.connect("localhost", 1883, 60) != 0:
        print("Couldn't connect to the mqtt broker")
        sys.exit(1)
    # Topic var
    topics = 'temperature'
    client.subscribe(topics)
    try:
        print("Press CTRL+C to exit...")
        client.loop_forever()
    except Exception:
        print("Caught an Exception, something went wrong...")
    finally:
        print("Disconnecting from the MQTT broker")
        client.disconnect()
