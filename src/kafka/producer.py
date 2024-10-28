import random
import time

from confluent_kafka import Producer

if __name__ == "__main__":
    # Conf for kafka connection
    conf = {'bootstrap.servers': 'localhost:9092','client.id': 'myproducer'}
    # Create the producer
    producer = Producer(conf)
    # Topic var
    topic = 'temperature'
    while True:
        # Create the msg
        temp = random.uniform(15.0, 40.0)
        msg = temp
        # Publish the msg
        print(f'Publishing: {msg}')
        producer.produce(topic, f'{msg}')
        # Wait 5 seconds and publish again
        time.sleep(1)
